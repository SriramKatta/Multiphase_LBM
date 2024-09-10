#pragma once
#include "cudahelp.cuh"
#include "lbmgrid.cuh"

#define TO1D(j, i, nx, ny) ((j) * (nx) + (i))

__global__ 
void initializegrid(lattice *grid, int nx, int ny)
{
  GRID_STRIDE_2D(startx, stridex, starty, stridey);
  for (int j = starty; j < ny; j += stridey)
    for (int i = startx; i < nx; i += stridex)
    {
      // top and bottom face
      if (j == 0 || j == ny - 1)
      {
        grid[TO1D(0, i, nx, ny)].flag = noslip_bdy;
        grid[TO1D(j, i, nx, ny)].flag = noslip_bdy;
      }
      // left face
      else if (i == 0)
      {
        grid[TO1D(j, 1, nx, ny)].flag = velocity_bdy;
      }
      // right face
      else if (i == nx - 1)
      {
        grid[TO1D(j, nx - 1, nx, ny)].flag = density_bdy;
      }
      // internal
      else
      {
        grid[TO1D(j, i, nx, ny)].flag = fluid_cell;
      }
    }
}