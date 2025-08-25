Welcome to SMART's documentation!
========================================

.. SMART documentation master file, created by
   sphinx-quickstart on Mon Agu 25 16:01:51 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Spatial multi-omic aggregation using graph neural networks and metric learning
=====================================================================================================================================================

.. toctree::
   :maxdepth: 1
   :caption: Contents:
   
   Installation
   Tutorial 1_Simulated_multi_omics_data_integration
   Tutorial 2_10x_human_lymph_node_data_integartion
   Tutorial 3_MISAR-seq_mouse_brain_data_integration
   Tutorial 4_P22_mouse_brain_section_data_integration
   Tutorial 5_10x_human_tonsil_multi_slice_integration


.. image:: ../Figures/Workflow-SMART.jpg
   :width: 1600 

Overview
========
Spatial multi-omics enables the exploration of tissue microenvironments and heterogeneity from the perspective of different omics modalities across distinct spatial domains within tissues. To jointly analyze the spatial multi-omics data, computational methods are desired to integrate multiple omics with spatial information into a unified space. Here, we present SMART (Spatial Multi-omic Aggregation using gRaph neural networks and meTric learning), a computational framework for spatial multi-omic integration. SMART leverages a modality-independent modular and stacking framework with spatial coordinates and adjusts the aggregation using triplet relationships. SMART excels at accurately identifying spatial regions of anatomical structures, compatible with spatial datasets of any type and number of omics layers, while demonstrating exceptional computational efficiency and scalability on large datasets. Moreover, a variant of SMART, SMART-MS, expands its capabilities to integrate spatial multi-omics data across multiple tissue sections. In summary, SMART provides a versatile, efficient, and scalable solution for integrating spatial multi-omics data.

Citation
========
Zhihua Du, Qiyi Chen, Weiliang Huang, Jinmiao Chen & Xubin Zheng. SMART: Spatial multi-omic aggregation using graph neural networks and metric learning. 2024.