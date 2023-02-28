#https://www.youtube.com/watch?v=sdQtM9BYxzo

#open jupyter notebook
#paste in the following codes
#---------------------------------------------------------------
!nvidia-smi
#---------------------------------------------------------------
%tensorflow_version 1.x
#---------------------------------------------------------------
import tensorflow as tf
tf.__version__
#---------------------------------------------------------------
!git clone https://github.com/TachibanaYoshino/AnimeGANv2.git
#---------------------------------------------------------------
%cd AnimeGANv2/
#---------------------------------------------------------------
!python test.py \
--checkpoint_dir checkpoint/generator_Hayao_weight \
--test_dir images \
--style_name results
#---------------------------------------------------------------
