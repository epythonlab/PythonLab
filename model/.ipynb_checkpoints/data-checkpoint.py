# create data model for pizza
class Pizza(object):
    _number_of_slices = int()
    _size = str()
    _price = float()
    
    def set_number_of_slices(self, no_slice):
        self._number_of_slices = no_slice
    
    def get_number_of_slices(self):
        return self._number_of_slices
    
    def set_size(self, size):
        self._size  = size
    def get_size(self):
        return self._size
    def set_price(self, price):
        self._price = price
    
    def get_price(self):
        return self._price
    