# -*- coding: utf-8 -*-

from odoo import models,fields

class Patient(models.Model):
     _name= "hospital.patient"
    patient_name = fields.Char(string='Name', required=True)
    patient_note= fields.char(string='Note')
    patient_age = fields.Integer('Age')
