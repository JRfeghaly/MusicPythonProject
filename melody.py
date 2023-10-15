from note import *
import musicalbeeps

class Melody:
    '''This is the Melody class'''
    
    def __init__(self, filename):
        '''str --> NoneType
        Creates a class of the Melody type
        >>> happy_birthday = Melody("birthday.txt")
        >>> len(happy_birthday.notes)
        25
        >>> print(happy_birthday.notes[5])
        1.0 F 4 sharp
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> len(hot_cross_buns.notes)
        17
        >>> print(happy_birthday.notes[10])
        0.5 A 4 natural
        '''
        
        fobj = open(filename,"r")
        song = fobj.read()
        fobj.close()
        
        temp_list = song.split('\n')
        self.title = temp_list[0]
        self.author = temp_list[1]
        
    
        temp_list2 = []
        for element in temp_list[2:]:
            temp_list2.append(element.split(' '))
            
        count = 0
        element_to_repeat = []
        notes = []
        element_to_repeat2 =[]
        is_false_before  = False
        
        for element in temp_list2:
            if element[-1] == 'true' and count == 0:
                
                count += 1
                element_to_repeat.append(element)
                element_to_repeat2.append(element)
                
            elif element[-1] == 'false':
                
                if count == 1:
                    
                    element_to_repeat.append(element)
                    is_false_before = True
                    
                elif count > 1:
                    for el in element_to_repeat2:
                        
                        if el[0][0] != '.':
                            dur = float(el[0])
                        else:
                            dur = float('0'+el[0])
                        
                        if el[1] == 'R':
                            for i in range(2):
                                notes.append(Note(dur, el[1]))
                            
                        else:
                            for i in range(2):
                                notes.append(Note(dur, el[1], int(el[2]), el[3].lower()))
                            
                    element_to_repeat2 = []
                    element_to_repeat=[]
                    count = 0
                    
                    if element[0][0] != '.':
                        dur = float(element[0])
                    else:
                        dur = float('0'+element[0])
                        
                    if element[1] == 'R':
                        notes.append(Note(dur, element[1]))
                        
                    else:
                        notes.append(Note(dur, element[1], int(element[2]), element[3].lower()))
                    
                else:
                    
                    if element[0][0] != '.':
                        dur = float(element[0])
                    else:
                        dur = float('0'+element[0])
                        
                    if element[1] == 'R':
                        notes.append(Note(dur, element[1]))
                        
                    else:
                        notes.append(Note(dur, element[1], int(element[2]), element[3].lower()))
    
                    element_to_repeat2 = []
                    element_to_repeat=[]
                
            elif element[-1] == 'true' and count == 1 and is_false_before:
                
                element_to_repeat.append(element)
                count = 0
                is_false_before  = False
                
                for i in range(2):
                    for el in element_to_repeat:
                        
                        if el[0][0] != '.':
                            dur = float(el[0])
                        else:
                            dur = float('0'+el[0])
                        
                        if el[1] == 'R':
                            notes.append(Note(dur, el[1]))
                        else:
                            notes.append(Note(dur, el[1], int(el[2]), el[3].lower()))
                        
                element_to_repeat = []
                element_to_repeat2 = []
                
            elif element[-1] == 'true' and count >= 1 and not is_false_before:
                element_to_repeat2.append(element)
                count += 1
                    
        self.notes = notes[:]
    
    def play(self, player):
        '''Player --> NoneType
        takes a music player object as explicit input, and calls the play
        method on each Note object of the notes instance attribute in order,
        passing the music player object each time as argument.
        '''
        
        for n in self.notes:
            n.play(player)
            
    def get_total_duration(self):
        ''' () --> float
        returns the total duration of the song as a float.
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.get_total_duration()
        13.0
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> hot_cross_buns.get_total_duration()
        8.0
        '''
        
        time = 0
        for n in self.notes:
            time += n.duration
    
        return time
    
    def lower_or_upper(self, is_upper):
        '''Boolean --> Boolean
        This function takes a boolean as an input and returns a boolean,\
        the boolean indicates if the input if we want to lower or upper the octave by 1.
        It returns False if we can't lower it or upper it and True if we can do it and changes the octaves.
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.lower_or_upper(False)
        True
        >>> happy_birthday.notes[5].octave
        3
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.lower_or_upper(True)
        True
        >>> happy_birthday.notes[5].octave
        5
        '''
        for n in self.notes:
        
            if n.pitch != 'R':
                
                if not is_upper and n.octave == n.OCTAVE_MIN  :
                    return False
                
                if is_upper and n.octave == n.OCTAVE_MAX:
                    return False
            
        new_note = []
        
        for n in self.notes:
            
            if is_upper:
                added_number = 1
                
            else:
                added_number = -1
                
            if n.pitch == 'R':
                new_note.append(Note(n.duration, n.pitch))
                
            else:
                new_note.append(Note(n.duration, n.pitch, n.octave + added_number, n.accidental))
            
        self.notes = new_note[:]
        return True
    
    def lower_octave(self):
        ''' () --> Boolean
        It reduces the octave of all notes in the song by 1 and returns True.
        However, a note’s octave cannot be reduced below 1.
        If that would happen,octaves would not be lowered and we would return False.
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.lower_octave()
        True
        >>> happy_birthday.notes[5].octave
        3
        '''
        
        return self.lower_or_upper(False)
    
    def upper_octave(self):
        '''() --> Boolean
        It increases the octave of all notes in the song by 1 and returns True.
        However, a note’s octave cannot be increased above 7.
        If that would happen,octaves would not be increased and we would return False.
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.upper_octave()
        True
        >>> happy_birthday.notes[5].octave
        5
        '''
        
        return self.lower_or_upper(True)
    
    def change_tempo(self, time_multiplicator):
        ''' float --> NoneType
        Takes one positive float as explicit input and returns
        nothing. It should multiply the duration of each note by the given float.
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.change_tempo(0.5)
        >>> happy_birthday.get_total_duration()
        6.5
        '''
        
        new_note_2 = []
        
        for n in self.notes:
            
            if n.pitch == 'R':
                new_note_2.append(Note(n.duration * time_multiplicator , n.pitch))
                
            else:
                new_note_2.append(Note(n.duration * time_multiplicator , n.pitch, n.octave, n.accidental))
                
        self.notes = new_note_2[:]
