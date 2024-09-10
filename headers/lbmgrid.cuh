#pragma once

enum celltype{
    fluid_cell = 0,
    noslip_bdy = 1,
    velocity_bdy = 2,
    density_bdy = 3
};


struct lattice
{
    celltype flag = fluid_cell;
    double u = 0.0;
    double v = 0.0 ;
    double density = 0.0;
    double pdf = 0.0;
    double pdf_old = 0.0;


};
