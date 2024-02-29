import pygame
import time

# Initialize Pygame
pygame.init()

# TODO:
# add functionality for recording data, 
# presenting multiple trials with varying indices of difficulty, 
# generating completion screens

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
#BLUE = (0, 0, 128)

# Set up the screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fitts' Law Experiment")

# set clock up
clock = pygame.time.Clock()

def start_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    return  # Exit the start screen function

        # Clear the screen
        screen.fill(WHITE)

        # Draw the button
        button_surface = pygame.Surface((150, 50))
        button_surface.fill(BLACK)
        button_rect = button_surface.get_rect(center=(screen_width / 2, screen_height / 2))
        screen.blit(button_surface, button_rect)

        # Draw text on the button
        font = pygame.font.Font(None, 32)
        text = font.render('START', True, GREEN)
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)

        pygame.display.flip()
        #clock.tick(30)

# Run the start screen
# start_screen()

def run_experiment():
    # Main experiment loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(WHITE)

        # Draw squares
        # rec1 = rec_1
        # rec2 = rec_2
        rect1 = pygame.draw.rect(screen, BLACK, (150, 200, 100, 100))
        rect2 = pygame.draw.rect(screen, BLACK, (300, 200, 100, 100))

        # Get start time
        start_time = time.time()

        # Loop for 10 clicks
        click_times = []
        i = 0
        while i < 30:
            pygame.display.flip() # Update the display 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if rect1.collidepoint(mouse_pos):
                        start_sample_time = time.time()
                    elif rect2.collidepoint(mouse_pos):
                        end_sample_time = time.time()
                        click_times.append(end_sample_time - start_sample_time)
                        i += 1
                        if i == 10:
                            rect1 = pygame.draw.rect(screen, WHITE, (150, 200, 100, 100))
                            rect1 = pygame.draw.rect(screen, BLACK, (150, 100, 100, 100))
                        if i == 20:
                            rect2 = pygame.draw.rect(screen, WHITE, (300, 200, 100, 100))
                            rect2 = pygame.draw.rect(screen, BLACK, (300, 300, 100, 100))
                        # pygame.display.flip()
                    
        # Get end time
        end_time = time.time()

        # Calculate time taken
        #First trial
        time_taken = end_time - start_time
        print("First Trial")
        for i in range(len(click_times)):
            if i < 10:
                print("First 10 clicks, " + str(i) + "th click: " + str(click_times[i]))
            if i < 20 and i >= 10 :
                print("Second 10 clicks, " + str(i) + "th click: " + str(click_times[i]))
            if i < 30 and i >= 20:
                print("Third 10 clicks, " + str(i) + "th click: " + str(click_times[i]))
            

        #print("Total time taken",time_taken)
        break


def run_experiment2():
    # Main experiment loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(WHITE)

        # Draw squares
        # rec1 = rec_1
        # rec2 = rec_2
        rect1 = pygame.draw.rect(screen, BLACK, (125, 200, 75, 75))
        rect2 = pygame.draw.rect(screen, BLACK, (325, 200, 75, 75))

        # Get start time
        start_time = time.time()

        # Loop for 10 clicks
        click_times = []
        i = 0
        while i < 30:
            pygame.display.flip() # Update the display 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if rect1.collidepoint(mouse_pos):
                        start_sample_time = time.time()
                    elif rect2.collidepoint(mouse_pos):
                        end_sample_time = time.time()
                        click_times.append(end_sample_time - start_sample_time)
                        i += 1
                        if i == 10:
                            rect1 = pygame.draw.rect(screen, WHITE, (125, 200, 75, 75))
                            rect1 = pygame.draw.rect(screen, BLACK, (125, 100, 75, 75))
                        if i == 20:
                            rect2 = pygame.draw.rect(screen, WHITE, (325, 200, 75, 75))
                            rect2 = pygame.draw.rect(screen, BLACK, (325, 300, 75, 75))
                        # pygame.display.flip()
                    
        # Get end time
        end_time = time.time()

        # Calculate time taken
        #First trial
        time_taken = end_time - start_time
        print("Second Trial")
        for i in range(len(click_times)):
            if i < 10:
                print("First 10 clicks, " + str(i) + "th click: " + str(click_times[i]))
            if i < 20 and i >= 10 :
                print("Second 10 clicks, " + str(i) + "th click: " + str(click_times[i]))
            if i < 30 and i >= 20:
                print("Third 10 clicks, " + str(i) + "th click: " + str(click_times[i]))
            

        #print("Total time taken",time_taken)
        break
    
def run_experiment3():
    # Main experiment loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(WHITE)

        # Draw squares
        # rec1 = rec_1
        # rec2 = rec_2
        rect1 = pygame.draw.rect(screen, BLACK, (100, 200, 50, 50))
        rect2 = pygame.draw.rect(screen, BLACK, (350, 200, 50, 50))

        # Get start time
        start_time = time.time()

        # Loop for 10 clicks
        click_times = []
        i = 0
        while i < 30:
            pygame.display.flip() # Update the display 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if rect1.collidepoint(mouse_pos):
                        start_sample_time = time.time()
                    elif rect2.collidepoint(mouse_pos):
                        end_sample_time = time.time()
                        click_times.append(end_sample_time - start_sample_time)
                        i += 1
                        if i == 10:
                            rect1 = pygame.draw.rect(screen, WHITE, (100, 200, 50, 50))
                            rect1 = pygame.draw.rect(screen, BLACK, (100, 100, 50, 50))
                        if i == 20:
                            rect2 = pygame.draw.rect(screen, WHITE, (350, 200, 50, 50))
                            rect2 = pygame.draw.rect(screen, BLACK, (350, 300, 50, 50))
                        # pygame.display.flip()
                    
        # Get end time
        end_time = time.time()

        # Calculate time taken
        #First trial
        time_taken = end_time - start_time
        print("Third Trial")
        for i in range(len(click_times)):
            if i < 10:
                print("First 10 clicks, " + str(i) + "th click: " + str(click_times[i]))
            if i < 20 and i >= 10 :
                print("Second 10 clicks, " + str(i) + "th click: " + str(click_times[i]))
            if i < 30 and i >= 20:
                print("Third 10 clicks, " + str(i) + "th click: " + str(click_times[i]))
            

        #print("Total time taken",time_taken)
        break

def run_experiment4():
    # Main experiment loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(WHITE)

        # Draw squares
        # rec1 = rec_1
        # rec2 = rec_2
        rect1 = pygame.draw.rect(screen, BLACK, (75, 200, 25, 25))
        rect2 = pygame.draw.rect(screen, BLACK, (375, 200, 25, 25))

        # Get start time
        start_time = time.time()

        # Loop for 10 clicks
        click_times = []
        i = 0
        while i < 30:
            pygame.display.flip() # Update the display 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if rect1.collidepoint(mouse_pos):
                        start_sample_time = time.time()
                    elif rect2.collidepoint(mouse_pos):
                        end_sample_time = time.time()
                        click_times.append(end_sample_time - start_sample_time)
                        i += 1
                        if i == 10:
                            rect1 = pygame.draw.rect(screen, WHITE, (75, 200, 25, 25))
                            rect1 = pygame.draw.rect(screen, BLACK, (75, 100, 25, 25))
                        if i == 20:
                            rect2 = pygame.draw.rect(screen, WHITE, (375, 200, 25, 25))
                            rect2 = pygame.draw.rect(screen, BLACK, (375, 300, 25, 25))
                        # pygame.display.flip()
                    
        # Get end time
        end_time = time.time()

        # Calculate time taken
        #First trial
        time_taken = end_time - start_time
        print("Fourth Trial")
        for i in range(len(click_times)):
            if i < 10:
                print("First 10 clicks, " + str(i) + "th click: " + str(click_times[i]))
            if i < 20 and i >= 10 :
                print("Second 10 clicks, " + str(i) + "th click: " + str(click_times[i]))
            if i < 30 and i >= 20:
                print("Third 10 clicks, " + str(i) + "th click: " + str(click_times[i]))
            

        #print("Total time taken",time_taken)
        break

def run_experiment5():
    # Main experiment loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(WHITE)

        # Draw squares
        # rec1 = rec_1
        # rec2 = rec_2
        rect1 = pygame.draw.rect(screen, BLACK, (50, 200, 10, 10))
        rect2 = pygame.draw.rect(screen, BLACK, (400, 200, 10, 10))

        # Get start time
        start_time = time.time()

        # Loop for 10 clicks
        click_times = []
        i = 0
        while i < 30:
            pygame.display.flip() # Update the display 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if rect1.collidepoint(mouse_pos):
                        start_sample_time = time.time()
                    elif rect2.collidepoint(mouse_pos):
                        end_sample_time = time.time()
                        click_times.append(end_sample_time - start_sample_time)
                        i += 1
                        if i == 10:
                            rect1 = pygame.draw.rect(screen, WHITE, (50, 200, 10, 10))
                            rect1 = pygame.draw.rect(screen, BLACK, (50, 100, 10, 10))
                        if i == 20:
                            rect2 = pygame.draw.rect(screen, WHITE, (400, 200, 10, 10))
                            rect2 = pygame.draw.rect(screen, BLACK, (400, 300, 10, 10))
                        # pygame.display.flip()
                    
        # Get end time
        end_time = time.time()

        # Calculate time taken
        #First trial
        time_taken = end_time - start_time
        print("Fifth Trial")
        for i in range(len(click_times)):
            if i < 10:
                print("First 10 clicks, " + str(i) + "th click: " + str(click_times[i]))
            if i < 20 and i >= 10 :
                print("Second 10 clicks, " + str(i) + "th click: " + str(click_times[i]))
            if i < 30 and i >= 20:
                print("Third 10 clicks, " + str(i) + "th click: " + str(click_times[i]))
            

        #print("Total time taken",time_taken)
        break

def next_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    return  # Exit the start screen function

        # Clear the screen
        screen.fill(WHITE)

        # Draw the button
        button_surface = pygame.Surface((150, 50))
        button_surface.fill(BLACK)
        button_rect = button_surface.get_rect(center=(screen_width / 2, screen_height / 2))
        screen.blit(button_surface, button_rect)

        # Draw text on the button
        font = pygame.font.Font(None, 32)
        text = font.render('NEXT GAME', True, WHITE)
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)

        pygame.display.flip()
        #clock.tick(30)
#next_screen()

def finish_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    pygame.quit()  # Exit the start screen function

        # Clear the screen
        screen.fill(WHITE)

        # Draw the button
        button_surface = pygame.Surface((150, 50))
        button_surface.fill(BLACK)
        button_rect = button_surface.get_rect(center=(screen_width / 2, screen_height / 2))
        screen.blit(button_surface, button_rect)

        # Draw text on the button
        font = pygame.font.Font(None, 32)
        text = font.render('FINSIHED', True, WHITE)
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)

        pygame.display.flip()
        #clock.tick(30)

# start_screen()
# run_experiment(rec_1=pygame.draw.rect(screen, BLACK, (100, 200, 100, 100)), rect_2 = pygame.draw.rect(screen, BLACK, (400, 200, 100, 100)))
# next_screen()
# start_screen()
# run_experiment(rec_1=pygame.draw.rect(screen, BLACK, (100, 200, 100, 100)), rect2 = pygame.draw.rect(screen, BLACK, (400, 200, 100, 100)))

start_screen()
run_experiment()
next_screen()
start_screen()
run_experiment2()
next_screen()
start_screen()
run_experiment3()
next_screen()
start_screen()
run_experiment4()
next_screen()
start_screen()
run_experiment5()
finish_screen()