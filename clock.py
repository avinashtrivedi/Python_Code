class Time (object):
    
    def __init__( self, hour=0, mins=0, secs=0 ):
        
        """ Construct a Time using hour,mins and secs. """
            
        self.__hour = hour
        self.__mins   = mins
        self.__secs  = secs
        
    def __repr__( self ):

        """ Return a string as the formal representation of Time in the form Class Time: hh:mm:ss. """

        out_str = "Class Time: {:02d}:{:02d}:{:02d}" \
            .format( self.__hour, self.__mins, self.__secs )

        return out_str
    
    def __str__( self ):

        """ Return a string (hh:mm:ss) to represent a Time. """

        out_str = "{:02d}:{:02d}:{:02d}" \
            .format( self.__hour, self.__mins, self.__secs )

        return out_str
    def from_str(self,time_str):

        """ 
        Update a time object by fetching hour ,mins and secs from
        
        string time_str which contains time in the form hh:mm:ss. 
        
        """

        hour, mins, secs = [ int( n ) for n in time_str.split( ':' )]
        
        self.__hour = hour
        self.__mins   = mins
        self.__secs  = secs