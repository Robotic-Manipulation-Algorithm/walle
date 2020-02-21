"""View a live feed from a connected D415.
"""

from walle.cameras import RealSenseD415

if __name__ == "__main__":
  with RealSenseD415(resolution="low") as cam:
    cam.view_feed()
