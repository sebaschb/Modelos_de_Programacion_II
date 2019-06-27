# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def error():
    return dict()

@auth.requires_login()
def tipo_estudio_manage():
    form = SQLFORM.smartgrid(db.t_tipo_estudio,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def formacion_academica_manage():
    form = SQLFORM.smartgrid(db.t_formacion_academica,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def experiencia_laboral_manage():
    form = SQLFORM.smartgrid(db.t_experiencia_laboral,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def hoja_vida_manage():
    form = SQLFORM.smartgrid(db.t_hoja_vida,onupdate=auth.archive)
    return locals()

