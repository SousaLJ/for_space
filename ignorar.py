
'''fps_button_30hz = Button('30hz.png', 400, 200, 1)
fps_button_60hz = Button('60hz.png', 560, 200, 1)
fps_button_120hz = Button('120hz.png', 720, 200, 1)
fps_button_144hz = Button('144hz.png', 780, 200, 1)
audio_button = Button('audio_button.png', 50, 100, 1)
display_button = Button('display_button.png', 225, 100, 1)
'''


'''
case 'audio_options':
            display.blit(audio_options_background, (0, 0))

            if display_button.draw(display):
                game_state = 'display_options'
            
            elif audio_button.draw(display):
                game_state = 'audio_options'

            elif back_to_menu_button.draw(display):
                game_state = 'menu'

            musica_text = font.render("Volume da Musica:", True, 'white')
            display.blit(musica_text, (100, 190))

            efeitos_text = font.render("Volume dos Efeitos:", True, 'white')
            display.blit(efeitos_text, (100, 290))

            volume_musica = musica_slider.draw(display)
            volume_efeitos = efeitos_slider.draw(display)
        
        case 'display_options':
            display.blit(display_options_background, (0, 0))

            brilho_text = font.render("Brilho:", True, 'white')
            display.blit(brilho_text, (185, 300))

            brilho = brilho_slider.draw(display)

            if audio_button.draw(display):
                game_state = 'audio_options'

            elif display_button.draw(display):
                game_state = 'display_options'
            
            elif back_to_menu_button.draw(display):
                game_state = 'menu'

            fps_text = font.render("Taxa de Atualizaçao:", True, 'white')
            display.blit(fps_text, (100, 200))  
            
            if fps_button_30hz.draw(display):
                fps = 30
            elif fps_button_60hz.draw(display):
                fps = 60
            elif fps_button_120hz.draw(display):
                fps = 120
            

'''