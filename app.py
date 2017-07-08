import math
import itertools
import cProfile, pstats

import pygame

WINDOW_SIZE = (1024, 768)
MAP_SIZE = (10, 10)
MAX_FPS = 0
FULLSCREEN_FLAGS = pygame.HWSURFACE | pygame.FULLSCREEN | pygame.DOUBLEBUF
NORMAL_FLAGS = 0

fullscreen = False 

# We need to create a screen before importing so that a video mode is set,
# and we are able to .convert() images.
pygame.init()
if fullscreen:
    flags = FULLSCREEN_FLAGS
else:
    flags = NORMAL_FLAGS
screen = pygame.display.set_mode(WINDOW_SIZE, flags)

import game
import fontutils
from colors import Color
import gameconsole
# These are imported to be used by the console
import states, leveltiles, enemies, playeritems


def alt_pressed(pressed_keys):
    return pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]

def shift_pressed(pressed_keys):
    return pressed_keys[pygame.K_LSHIFT] or pressed_keys[pygame.K_RSHIFT]

def exit_event(event, pressed_keys):
    return (event.type == pygame.QUIT) or \
           (event.type == pygame.KEYDOWN and \
                event.key == pygame.K_q and alt_pressed(pressed_keys))

def center_fix(outer_rect, inner_rect):
    return ((outer_rect.width - inner_rect.width) // 2, (outer_rect.height - inner_rect.height) // 2)

def fixed_mouse_pos(ds_center_fix):
    pos = pygame.mouse.get_pos()
    return (pos[0] - ds_center_fix[0], pos[1] - ds_center_fix[1])

class App:
    console_namespace_additions = {
        "math": math,
        "states": states,
        "leveltiles": leveltiles,
        "enemies": enemies,
        "playeritems": playeritems
    }
    def __init__(self, screen=None, use_dirty_rects=False):
        self.screen = screen
        self.console = gameconsole.GameConsole(self)
        self.game = game.GameEngine(screen_size=WINDOW_SIZE, screen=self.screen, 
                                    mapsize=MAP_SIZE)
        self.use_dirty_rects = use_dirty_rects

    def run(self, fullscreen=fullscreen):
        player = self.game.player
        last_state = current_state = None
        show_fps = False; fpsfont = fontutils.get_sysfont("Monospace", 32); force_show_fps = False
        max_fps_vals = itertools.cycle((0, 60, 150))
        max_fps = next(max_fps_vals)
        act_max_fps = max_fps
        console_enabled = False
        # Console functions
        def get_level():
            return current_state.level
        def spawn_enemy(cls, col, row, count=1):
            lvl = get_level()
            for _ in range(count):
                lvl.sprites.append(cls(lvl, lvl.layout[row][col]))
        def drop_item(item_cls, pos):
            lvl = get_level()
            lvl.sprites.append(playeritems.DroppedItem(lvl, pos, item_cls))
        def get_sprites_by_class(cls):
            return get_level().get_sprites_if(lambda sprite: type(sprite) is cls)
        def get_sprite_by_class(cls):
            return get_sprites_by_class(cls)[0]
        def give(arg):
            cls = getattr(playeritems, arg) if isinstance(arg, str) else arg
            return player.inventory.add_item(cls(player))
        console_functions = [get_level, spawn_enemy, get_sprite_by_class]
        self.console_namespace_additions.update({func.__name__: func for func in console_functions})

        # Main loop
        pause = False
        ticks = 0
        clock = pygame.time.Clock()
        running = True
        while running:
            # Event
            mouse_pos = pygame.mouse.get_pos()
            pressed_keys = pygame.key.get_pressed()
            events = pygame.event.get()
            for event in events:
                if exit_event(event, pressed_keys):
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F2:
                        console_enabled = not console_enabled
                    elif event.key == pygame.K_F3:
                        show_fps = not show_fps
                        if show_fps: force_show_fps = True
                    elif event.key == pygame.K_F11:
                        fullscreen = not fullscreen
                        if fullscreen:
                            flags = FULLSCREEN_FLAGS
                        else:
                            flags = NORMAL_FLAGS
                        pygame.display.set_mode(WINDOW_SIZE, flags)
                    elif shift_pressed(pressed_keys):
                        # These are valid characters, and the user may need them
                        # otherwise e.g. shift+p=P may be muted and a pause may be created
                        # instead
                        if not console_enabled: 
                            if event.key == pygame.K_f:
                                act_max_fps = next(max_fps_vals)
                                print("Set max FPS to", act_max_fps)
                            elif event.key == pygame.K_h:
                                self.game.vars["enable_enemy_hp_bars"] = not self.game.vars["enable_enemy_hp_bars"]
                            elif event.key == pygame.K_p:
                                pause = not pause
            if pause:
                continue
            last_state = current_state
            current_state = self.game.top_state
            if current_state is None: 
                raise RuntimeError("No current state")
            if last_state != current_state and last_state is not None and not last_state.deactivated:
                last_state.pause()
            if current_state.paused:
                current_state.resume()

            # Some events (e.g. letter keypresses) are muted by the console,
            # so we need to process it first.
            if console_enabled:
                constatus = self.console.update(mouse_pos, pressed_keys, events)

            self.game.handle_events(current_state, events, pressed_keys, mouse_pos)
            pygame.event.pump()

            # Logic

            self.game.update(current_state)
            
            # Draw

            self.screen.fill(Color.Black)

            self.game.draw(current_state, self.screen)

            if console_enabled:
                if constatus is self.console.Status.Interpret:
                    namespace = locals()
                    namespace.update(self.console_namespace_additions)
                    self.console.interpret_current(namespace)
                self.console.draw(self.screen)
            if show_fps:
                if not ticks % 120 or force_show_fps:
                    current_fps = round(clock.get_fps())
                    render = fontutils.get_text_render(fpsfont, str(current_fps), False, Color.Red, dolog=False)
                fps_rect = render.get_rect()
                fps_rect.x = self.screen.get_width() - render.get_width()
                self.screen.blit(render, fps_rect)

            pygame.display.flip()

            if current_state is not None and current_state.lazy_state:
                max_fps = 60
            else:
                max_fps = act_max_fps
            clock.tick(max_fps)
            ticks += 1

        pygame.quit()


if __name__ == "__main__":
    print("Screen size:", WINDOW_SIZE)
    profiler = cProfile.Profile()
    profiler.enable()
    app = App(screen)
    app.run()
    profiler.disable()
    profiler.dump_stats("profile.stats")
    stats = pstats.Stats("profile.stats")
    stats.strip_dirs(); stats.sort_stats("ncalls")
    #stats.print_stats()

