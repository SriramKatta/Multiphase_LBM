#include <tuple>

#include "computehelp.cuh"
#include "thrust/host_vector.h"
#include "thrust/device_vector.h"

int main(int argc, char const *argv[])
{
  auto [thpblk, blks] = getgpuconfig2D();

  int sizex = 400;
  int sizey = 80;

  int nx = sizex + 2;
  int ny = sizey + 2;
  thrust::host_vector<lattice> grid(nx * ny);
  thrust::device_vector<lattice> grid_dev = grid;
  lattice* grid_ptr = thrust::raw_pointer_cast(grid_dev.data());
  initializegrid<<<blks, thpblk>>>(grid_ptr, nx, ny);
  grid = grid_dev;
}
