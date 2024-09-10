#include <tuple>

#include "computehelp.cuh"
#include "thrust/host_vector.h"
#include "thrust/device_vector.h"
#include "vtkhelper.hpp"

void printhvec(auto & vec){
  for (auto &&i : vec)
  {
    std::cout << i << " ";
  }
  std::cout << std::endl;
  
}

int main(int argc, char const *argv[])
{
  auto [thpblk, blks] = getgpuconfig2D();

  int sizex = 4000;
  int sizey = 800;

  int nx = sizex + 2;
  int ny = sizey + 2;
  thrust::host_vector<D2Q9::lattice> grid(nx * ny);
  thrust::device_vector<D2Q9::lattice> grid_dev = grid;
  D2Q9::lattice* grid_ptr = thrust::raw_pointer_cast(grid_dev.data());
  initializegrid<<<blks, thpblk>>>(grid_ptr, nx, ny);
  initializepdf<<<blks, thpblk>>>(grid_ptr, nx, ny);
  grid = grid_dev;
  vtkWriter("50", nx, ny, grid);

}
