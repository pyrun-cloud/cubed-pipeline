import logging

import cubed
import cubed.array_api as xp
import cubed.random
from cubed.diagnostics.history import HistoryCallback
from cubed.diagnostics.timeline import TimelineVisualizationCallback

logging.getLogger("urllib3.connectionpool").setLevel(logging.ERROR)

if __name__ == "__main__":
    a = cubed.random.random((10000, 10000), chunks=(1000, 1000))
    b = cubed.random.random((10000, 10000), chunks=(1000, 1000))
    c = xp.add(a, b)

    history_callback = HistoryCallback()
    timeline_callback = TimelineVisualizationCallback()

    cubed.to_zarr(c, store=None, callbacks=[history_callback, timeline_callback])
    
