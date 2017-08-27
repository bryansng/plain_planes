import pygame

from pygame.sprite import Group
from pygame.sprite import GroupSingle

import game_functions as gf
from settings import Settings
from ship import Ship
from bullet import ShipBullet
from parachute import Parachute
from bullet import HelicopterBullet
from hostile import Helicopter
from hostile import Rocket
from hostile import AdvancedHelicopter
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from background import Background

def run_game():
	# Initialize pygame
	pygame.init()
	
	# Initializing all the game classes.
	ai_settings = Settings()
	stats = GameStats(ai_settings)
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Hostile Takeover")
	
	bg = Background(ai_settings, screen)
	sb = Scoreboard(ai_settings, screen, stats)
	ship = Ship(ai_settings, screen, sb)
	
	# Actually, there is no need to import their classes into this file.
	parachutes = Group()
	
	# Actually, there is no need to import their classes into this file.
	helis = Group()
	rockets = Group()
	ad_helis = Group()
	shipbullets = Group()
	helibullets = Group()
	
	# Create buttons to be pressed.
	play_button_mm = Button(ai_settings, screen, 'Play')
	stats_button_mm = Button(ai_settings, screen, 'Statistics')
	quit_button_mm = Button(ai_settings, screen, 'Quit Game')
	
	resume_button_esc = Button(ai_settings, screen, 'Resume')
	restart_button_esc = Button(ai_settings, screen, 'Restart Game')
	stats_button_esc = Button(ai_settings, screen, 'Statistics')
	exit_button_esc = Button(ai_settings, screen, 'Exit to Main Menu')
	#settings_button = Button(ai_settings, screen, 'Settings')
	
	# Reposition Main menu buttons based on the button above it.
	space_btw_buttons = 8
	stats_button_mm.rect.y += space_btw_buttons + play_button_mm.rect.height
	stats_button_mm.msg_image_rect.centery = stats_button_mm.rect.centery
	quit_button_mm.rect.y = space_btw_buttons + stats_button_mm.rect.y + stats_button_mm.rect.height
	quit_button_mm.msg_image_rect.centery = quit_button_mm.rect.centery
	
	# Reposition Esc menu buttons based on the button above it.
	restart_button_esc.rect.y += space_btw_buttons + resume_button_esc.rect.height
	restart_button_esc.msg_image_rect.centery = restart_button_esc.rect.centery
	stats_button_esc.rect.y = space_btw_buttons + restart_button_esc.rect.y + restart_button_esc.rect.height
	stats_button_esc.msg_image_rect.centery = stats_button_esc.rect.centery
	exit_button_esc.rect.y = space_btw_buttons + stats_button_esc.rect.y + stats_button_esc.rect.height
	exit_button_esc.msg_image_rect.centery = exit_button_esc.rect.centery
	
	#settings_button.rect.y = space_btw_buttons + 
	#settings_button.msg_image_rect.centery = settings_button.rect.centery
	
	#print(pygame.display.Info())
	
	# Creating list for rocket and ad_helis.
	rockets_hits_list = []
	ad_helis_hits_list = []
	
	# Ensures that the events, internals and screen is always running.
	while True:
		# In charge of checking all game events prior to screen updates.
		gf.check_events(ai_settings, screen, ship, shipbullets, helis, helibullets, rockets, rockets_hits_list, ad_helis, ad_helis_hits_list, stats, play_button_mm, stats_button_mm, quit_button_mm, resume_button_esc, restart_button_esc, stats_button_esc, exit_button_esc, sb)
		
		# Updates all game internal functions prior to screen updates and only when game is active.
		if stats.game_active:
			gf.update_internals(ai_settings, screen, ship, shipbullets, parachutes, helis, helibullets, rockets, rockets_hits_list, ad_helis, ad_helis_hits_list, stats, sb)
		
		# Updates the screen with all the objects and projectiles.
		gf.update_screen(ai_settings, screen, ship, shipbullets, parachutes, helis, helibullets, rockets, ad_helis, stats, play_button_mm, stats_button_mm, quit_button_mm, resume_button_esc, restart_button_esc, stats_button_esc, exit_button_esc, sb, bg)
		


run_game()
