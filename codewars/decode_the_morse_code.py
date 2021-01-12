def decodeMorse(morseCode):
    words = '.... . -.--   .--- ..- -.. .'.split('   ')
    # words = morseCode.split('   ')
    
    return ' '.join([''.join([MORSE_CODE[s] for s in word.split(' ')]) for word in words])
     
    return morseCode.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')



if __name__ == '__main__':

    print (decodeMorse('.... . -.--   .--- ..- -.. .') == 'HEY JUDE')
