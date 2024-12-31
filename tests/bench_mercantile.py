import os
import random
import time
import argparse
from multiprocessing import Pool
import mercantile

def run_single(n=1e5):
    for _ in range(n):
        lvl = random.randrange(2, 29)
        coords = (random.uniform(-85.05, 85.05), random.uniform(-180., 180.))
        
        tile = mercantile.tile(*coords, lvl)
        qk = mercantile.quadkey(tile)
        mercantile.neighbors(tile)
        mercantile.parent(tile)
        mercantile.lnglat(tile.x, tile.y)
        
        
def run(n=1e6, workers=os.cpu_count()):
    t0 = time.monotonic()
    with Pool(workers) as pool:
        pool.map(run_single, [int(n / workers)] * workers)
    t1 = time.monotonic()
    
    print(f'Took {t1 - t0}')
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser('QuadKey benchmarking')
    parser.add_argument('-n', type=int, default=1e7, help='Total iterations')
    parser.add_argument('-j', type=int, default=os.cpu_count(), help='Number of CPU processes')
    args = parser.parse_args()
    
    print(f'Running {args.n} iterations on {args.j} workers')
    run(args.n, args.j)  # 30.536s