import musicalbeeps

class Note:
    ''' This is the Note class'''
    
    OCTAVE_MIN = 1
    OCTAVE_MAX = 7
    
    def __init__(self, duration, pitch, octave = 1, accidental = 'natural'):
        
        ''' float, str, int, str --> NoneType
        Creates an object of type Note
        >>> note = Note(2.0, "B", 4, "natural")
        >>> note.pitch
        'B'
        '''
        
        if type(duration) is not float or duration <= 0:
            raise AssertionError('invalid input for duration')
        
        if type(pitch) is not str or pitch not in ['A','B','C','D','E','F','G','R']:
            raise AssertionError('invalid input for pitch')
        
        if type(octave) is not int or not self.OCTAVE_MIN <= octave <= self.OCTAVE_MAX:
            raise AssertionError('invalid input for octave')
        
        if type(accidental) is not str or accidental not in ['sharp' ,'flat' ,'natural']:
            raise AssertionError('invalid input for accidental value')
        
        self.duration = duration
        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental
        
    def __str__(self):
        ''' ()--> str
        returns the note of the file
        >>> note = Note(2.0, "B", 4, "natural")
        >>> print(note)
        2.0 B 4 natural
        '''
        
        return str(self.duration) + ' ' + self.pitch + ' ' + str(self.octave) + ' ' + self.accidental
    
    def play(self, player):
        ''' player --> NoneType
            that takes one explicit input corresponding to a music player object
            The method should construct the note string then pass the note string and duration to it
            so that the note can be played through the speakers.
            If the note is a rest note (pitch R), then the note string should be the single word 'pause'.
            '''
        
        player = musicalbeeps.Player()
        
        acc_signs = {'natural' : '', 'sharp' : '#', 'flat': 'b'}
        
        if self.pitch == 'R':
            player.play_note('pause', self.duration)
            
        else:
            player.play_note(self.pitch + str(self.octave) + acc_signs[self.accidental], self.duration)