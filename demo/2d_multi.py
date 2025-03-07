import numpy as np
import anim

# === 2D Animation =========================================================

class myAnimation(anim.plane.view):

  def __init__(self, W, color):

    super().__init__(W)

    self.padding = 0.01

    self.x0 = 0.5
    self.y0 = 0.5
    self.R = 0.25
    self.r = 0.01

    self.add(anim.plane.ellipse, 'E0',
      position = [self.x0, self.y0],
      major = 0.005,
      minor = 0.005,
      colors = ('white', None),
    )

    self.add(anim.plane.circle, 'C0',
      position = [self.x0, self.y0],
      radius = self.R,
      colors = (None, 'grey'),
      thickness = 2,
      linestyle = '--'
    )

    self.add(anim.plane.circle, 'C',
      position = [self.x0 + self.R, self.y0],
      radius = self.r,
      colors = (color, None),
    )

  def update(self, t):
    
    # Update timer display
    super().update(t)

    # Update position
    x = self.x0 + self.R*np.cos(t.time)
    y = self.y0 + self.R*np.sin(t.time)
    self.item['C'].position = [x, y]

# === Main =================================================================

W = anim.window('Multiple animation')

# Add animation
W.add(myAnimation(W, 'red'))
W.add(myAnimation(W, 'green'))

# Allow backward animation
W.allow_backward = True
W.allow_negative_time = False

W.show()