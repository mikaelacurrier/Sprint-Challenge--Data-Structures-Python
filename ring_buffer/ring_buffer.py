class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # add to storage based on current (index)
    self.storage[self.current] = item

    # check to see if the current is 
    if self.current + 1 < self.capacity:
      self.current += 1
    else:
      self.current = 0

  def get(self):
    return [item for item in self.storage if item is not None]