class StoreDictionary:

    dictionary: dict # usage of dictionary

    def __init__(self, dictionary, version, price_decimal=2): # init() method

        self.dictionary = dictionary # public class attribute of the menu dict

        self.version = version # public class attribute of the menu version

        self.__price_decimal = price_decimal # private class attribute of price's decimal places


    def __repr__(self): # repr() method

        return "Menu(%s)" % self.dictionary


    def __round__(self, price): # magic method to round the input price

        price = float(price)

        return round(price, self.__price_decimal)


  # User-defined function: whether the file exists or not

  # Private class method

    def __check_file_exists(self, filename):

        try: # usage of try to read the file

            f = open(filename)

            f.close()

        except Exception:

            return 0

        return 1


  # Writing to file when we tries to save the file

  # Public class method

    def write_file(self, filename):

        file = open(filename, 'w')

        for i in self.dictionary:

            file.write(i + ' ' + str(self.dictionary[i]) + '\n') # write the data for tuple format


  # Reading file and storing values to dictionary

  # Public class method

    def read_stored_file(self, filename):

        while True:
            if self.__check_file_exists(filename): # function returns 0 if no file found

                break

            print('Enter: the input file ' + filename + ' not found')

            return None

        file = open(filename, 'r')

        for i in file:

            flr = i.strip().split(' ')

            if i != '':

                name, cost = tuple(flr) # usage of tuple

                self.dictionary[name.strip()] = float(cost.strip())

        file.close()

        return file