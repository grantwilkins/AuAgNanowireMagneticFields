# Au-Ag Nanowire with Applied MagneticFields
Research project exploring the conductivity of gold and silver nanowire with magnetic fields applied, using the SIESTA and TranSIESTA programming languages,

## Abstract
With the prevalence of shrinking devices and the recent study by Thapa and Pandey concerning the synthesis of Au-Ag Nanostructures that exhibit superconductivity, a computational study about Au-Ag wires was needed (Thapa and Pandey, 2018). While their methods included lab synthesis, this study works to manufacture a similar study through computational simulation. In this study, SIESTA and TranSIESTA were used to synthesize temperature-independent results from a gold and silver wire using the principles of quantum mechanics and molecular dynamics (Soler et al., 2002; Stokbro, Taylor, Brandbyge, and Ordejon, 2006). By varying an applied magnetic field, different current and voltage results were developed for discrete cases. While complete replication of the Thapa and Pandey study was not possible in the computational setting due to temperature independence, the results revealed a lack of interesting conductive patterns and showed that the configuration tested has very little use in terms of device fabrication.

## Installation
For a guide to the installation of the SIESTA software look at the [README](https://github.com/grantwilkins/LithiumNanowireExperiments) in my other repository for a different project.

## How to Use
While the abstract might detail some of the findings and also a little bit about the inspiration of this project, using the files requires an installed version of SIESTA and TranSIESTA and each file uses a different part of the software and is a separate experiment.

Basically, for each file a graph can be produced for current versus voltage to show the conductive behavior of the molecule.
The naming dichotomy is that files with *Magnetic* in the name have a magnetic field. *Up* or *Down* in the file name means a positive or negative magnetic field. And the numbers on the end mean how much magnetic field, so *01* = 0.1, *1* = 1.0, *10* = 10 and so on. 

Voltage values are set in the VOLTAGE.fdf file. To then run SIESTA using the file consult the README linked earlier.
