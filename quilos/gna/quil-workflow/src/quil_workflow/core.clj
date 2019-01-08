(ns quil-workflow.core
  (:require [quil.core :as q])
  (:require [quil-workflow.dynamic :as dynamic]))
    
(q/defsketch example                
  :title "Oh so many grey circles"
  :setup dynamic/setup           
  :draw dynamic/draw              
  :size [800 600])                
