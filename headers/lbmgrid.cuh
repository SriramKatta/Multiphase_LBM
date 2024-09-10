#pragma once

#include "thrust/device_vector.h"

namespace D2Q9
{

  enum celltype
  {
    fluid_cell = 0,
    noslip_bdy = 1,
    velocity_bdy = 2,
    density_bdy = 3
  };

  struct lattice
  {
    celltype flag = fluid_cell;
    double u = 0.0;
    double v = 0.0;
    double density = 0.0;
    double pdf[9] = {0.0};
    double pdf_old[9] = {0.0};
  };

  thrust::device_vector cu{-1, 0, 1, -1, 0, 1, -1, 0, 1};
  thrust::device_vector cv{-1, -1, -1, 0, 0, 0, 1, 1, 1};
  thrust::device_vector wq{1.0 / 36, 1.0 / 9, 1.0 / 36, 1.0 / 9, 4.0 / 9, 1.0 / 9, 1.0 / 36, 1.0 / 9, 1.0 / 36};

}