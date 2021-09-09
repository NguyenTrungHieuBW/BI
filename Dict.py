# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 01:32:20 2021

@author: Admin
"""

from googletrans import Translator, constants

def dictionary():
    my_dict = constants.LANGUAGES
    my_dict["zh"]="chinese"
    my_dict["cn"]="chinese"
    my_dict["wo"]="wolof"
    my_dict["nb"]="ndebele"
    my_dict["sh"]="shanghai"
    my_dict["xx"]="no data"
    my_dict["bo"]="bo"
    my_dict["ab"]="ab"
    my_dict["bm"]="malay"
    my_dict["rw"]="kinyarwanda"
    my_dict["qu"]="no data"
    my_dict["jv"]="javanese"
    my_dict["ay"]="igpay atinlay"
    my_dict["iu"]="iu"
    my_dict["kw"]="kuwait"
    my_dict["nv"]="neveda"
    my_dict["ty"]="tahitian"
    my_dict["as"]="austronesian"
    my_dict["gn"]="guarani"
    my_dict["cr"]="spanish"
    my_dict["oc"]="no data"
    my_dict["to"]="no data"
    my_dict["ce"]="no data"
    my_dict["tt"]="tatar"
    my_dict["se"]="sami"
    my_dict["dz"]="arabic"
    my_dict["ln"]="no data"
    my_dict["sa"]="arabic"
    my_dict["tk"]="no data"
    my_dict["sc"]="no data"
    my_dict["ff"]="no data"
    my_dict["ug"]="no data"
    my_dict["br"]="portuguese"
    my_dict["sg"]="chinese"
    my_dict["ki"]="no data"
    my_dict["tn"]="tswana"
    my_dict["fo"]="faroese"
    my_dict["bi"]="no data"
    my_dict["mh"]="no data"
    return my_dict
