# Project descriptions - draft portfolio content

Temporary source material migrated from the GitHub profile README. These descriptions are intended to be refined and reused when building the project/software sections of the personal website.

## Computer vision, SLAM & robotics

### slam-primitives

Public repository: https://github.com/PeterCalifano/slam-primitives

Header-only C++20 library providing reusable data structures and components for visual-SLAM frontends, including feature tracks, bundles and covisibility structures. Designed as an installable, dependency-light package with optional CUDA, ROS 2 and language bindings.

### pyramidal-klt-for-space-nav

Private repository.

C++20 pyramidal KLT feature-tracking library for visual navigation, with MATLAB-codegen KLT/MSAC kernels, an OpenCV-based tracking pipeline, Python/MATLAB bindings and an optional ROS 2 overlay. It also includes reproducible demos on lunar imagery for end-to-end showcase of the frontend pipeline.

### space-nav-frontend

Private repository.

Visual-navigation frontend used to develop and integrate feature tracking, geometric vision and related perception components for the broader spacecraft navigation architecture.

## Spacecraft navigation and estimation

### gtsam-space-nav

Private repository.

C++20 extension library for spacecraft navigation on top of GTSAM, including dynamics and propagation utilities, process-noise handling, measurement and maneuver factors, and optional Python/MATLAB wrappers.

### EstimationGears for SpaceNav

Public repository: https://github.com/PeterCalifano/EstimationGears_for_SpaceNav

Collection of reusable MATLAB and C++ building blocks for spacecraft navigation estimators, progressively organized and refactored from research code developed across different projects.

### space-nav-backend

Private repository.

Navigation backend combining MATLAB algorithms with a standalone C++/CUDA library, wrapper infrastructure and an optional ROS 2 overlay.

### space-nav-loop-closures

Private repository.

Research repository for loop-closure detection and geometric validation in visual SLAM for small-body navigation.

## Space environment and models simulation

### SimulationGears for SpaceNav

Public repository: https://github.com/PeterCalifano/SimulationGears_for_SpaceNav

Simulation infrastructure for spacecraft navigation research, combining a MATLAB-based simulation environment with a growing native C++20, CUDA and ROS 2 software stack.

### space-nav-shape-reconstruction

Private repository.

Research and software for shape reconstruction and mapping of poorly characterized bodies, intended for integration with navigation and SLAM pipelines.

## Event-based vision

### event-based-centroiding

Private repository.

C++20 and Python project for event-based centroid estimation, with optional CUDA and oneTBB support and installable C++ and Python package structures.

### EventDataGenerationLib

Private repository.

Utilities and experiments for generating event-camera data and synthetic event streams for algorithm development and evaluation.

### event-cameras-primitives

Public repository: https://github.com/PeterCalifano/event-cameras-primitives

Status: WIP.

Early-stage C++/CUDA foundation for reusable event-camera processing components. The public repository is still being reorganized from the common project template.

## Machine learning & deployment

### pyTorchAutoForge

Public repository: https://github.com/PeterCalifano/pyTorchAutoForge

Tools for PyTorch model development, experiment tracking, optimization and deployment. Includes integration with MLflow and Optuna together with ONNX, TensorRT and embedded/Jetson-oriented workflows.

### torchAutoForge-deploy

Public repository: https://github.com/PeterCalifano/torchAutoForge-deploy

Status: WIP.

Companion deployment library for pyTorchAutoForge, separating inference and runtime integration from the model-development stack. Current work focuses on C++ ONNX Runtime inference, installable CMake packaging and Python/MATLAB binding support.

## Rendering & sensor simulation

### computer-graphics-primitives

Public repository: https://github.com/PeterCalifano/computer-graphics-primitives

Dependency-light C++20 foundation for reusable computer-graphics, rendering and physically based sensor-simulation components.

### spectra-rt

Private repository.

GPU-accelerated rendering framework for physically based and radiometric simulation of space scenes, developed with C++, CUDA and NVIDIA OptiX.

## Development tools

### cpp_cuda_template_project

Public repository: https://github.com/PeterCalifano/cpp_cuda_template_project

Reusable CMake project template for modern C++20 and GPU-accelerated libraries, with optional CUDA, OptiX, TensorRT, Python/MATLAB bindings, testing, documentation, profiling and CI support.

### AutoCodegenTools4MATLAB

Public repository: https://github.com/PeterCalifano/AutoCodegenTools4MATLAB

Utilities for streamlining MATLAB and Simulink code generation workflows, including automated generation of Interface Control Documents.
