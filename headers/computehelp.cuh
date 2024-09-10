#pragma once

#include "cudahelp.cuh"
#include "lbmgrid.cuh"


__global__ 
void initializegrid(D2Q9::lattice *grid, int nx, int ny)
{
  GRID_STRIDE_2D(startx, stridex, starty, stridey);
  for (int j = starty; j < ny; j += stridey)
    for (int i = startx; i < nx; i += stridex)
    {
      // top and bottom face
      if (j == 0 || j == ny - 1)
      {
        grid[TO1D(0, i, nx, ny)].flag = D2Q9::noslip_bdy;
        grid[TO1D(j, i, nx, ny)].flag = D2Q9::noslip_bdy;
      }
      // left face
      else if (i == 0)
      {
        grid[TO1D(j, i, nx, ny)].flag = D2Q9::velocity_bdy;
      }
      // right face
      else if (i == nx - 1)
      {
        grid[TO1D(j, i, nx, ny)].flag = D2Q9::density_bdy;
      }
      // internal
      else
      {
        grid[TO1D(j, i, nx, ny)].flag = D2Q9::fluid_cell;
      }
    }
}


__global__ 
void initializepdf(D2Q9::lattice *grid, int nx, int ny)
{
  GRID_STRIDE_2D(startx, stridex, starty, stridey);
  for (int j = starty; j < ny; j += stridey)
    for (int i = startx; i < nx; i += stridex)
    {
      if(grid[TO1D(j,i,nx,ny)].flag == D2Q9::noslip_bdy)
        continue;
      
    }
}