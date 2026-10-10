# Research

<!--
Appears on research.html. Page order: Navigation & mapping (then Bennu and Apophis
videos), Perception (then Itokawa tracking), Multi-sensor estimation, Simulation &
validation. Media placement, titles and tags stay in build.py. Keep the ## section names
unchanged: the builder uses them as keys. Comments like this are not published.
-->

## Introduction

<!--
Below Research interests at the top of the page. One paragraph; line breaks are folded.
-->

Visual navigation, mapping, and multi-sensor state estimation for spacecraft and robots
operating with limited prior knowledge of their surroundings.

## Navigation & mapping

<!--
Bullets beneath SLAM for small-body exploration, above the Bennu and Apophis videos.
Each - starts a bullet. Indented continuation lines belong to that bullet. Add or remove
bullets here; headings and tags stay in build.py.
-->

- Joint estimation of spacecraft motion and environmental geometry from visual
  observations.
- Integration of factor-graph smoothing, recursive filtering, and orbital dynamics for
  proximity navigation.
- Metric-scale observability and uncertainty under target rotation, variable illumination,
  and uncertain dynamics.
- Computational efficiency and estimation consistency within onboard processing
  constraints.

## Perception

<!--
Bullets beneath Visual measurements for navigation, above the Itokawa tracking GIF. Each
- starts a bullet. Indented continuation lines belong to that bullet. Add or remove
bullets here; headings and tags stay in build.py.
-->

- Feature tracking and multi-view geometry for motion estimation and scene reconstruction.
- Photometric modelling of visual measurements under variable illumination and viewing
  geometry.
- Learning-based correction of image-derived navigation measurements, including target
  centroid estimates.
- Event-based vision for odometry and localization.

## Multi-sensor estimation

<!--
Bullets beneath State estimation for robotic platforms, after the Itokawa figure. Each -
starts a bullet. Indented continuation lines belong to that bullet. Add or remove
bullets here; headings and tags stay in build.py.
-->

- Tightly coupled fusion of visual, inertial, joint-state, and contact measurements.
- Motion estimation for humanoids with free-floating or underactuated bases.
- Complementary geometric, kinematic, and contact constraints for localization.
- Assessment of sensor contributions, estimation accuracy, and uncertainty.

## Simulation & validation

<!--
Bullets beneath Modelling and evaluation of navigation systems, in the final research
section. Each - starts a bullet. Indented continuation lines belong to that bullet. Add
or remove bullets here; headings and tags stay in build.py.
-->

- Spacecraft dynamics models with gravity, solar-radiation pressure, and manoeuvres.
- Synthetic sensor measurements for navigation-system development and validation.
- Spectral and radiometric rendering under variable illumination, surface properties, and
  viewing geometry.
- Monte Carlo assessment of estimation errors, uncertainty, and computational cost.
