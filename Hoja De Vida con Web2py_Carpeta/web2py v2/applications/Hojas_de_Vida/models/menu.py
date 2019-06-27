response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Hoja Vida'),URL('default','hoja_vida_manage')==URL(),URL('default','hoja_vida_manage'),[]),
(T('Formacion Academica'),URL('default','formacion_academica_manage')==URL(),URL('default','formacion_academica_manage'),[]),
(T('Experiencia Laboral'),URL('default','experiencia_laboral_manage')==URL(),URL('default','experiencia_laboral_manage'),[]),
(T('Tipo Estudio'),URL('default','tipo_estudio_manage')==URL(),URL('default','tipo_estudio_manage'),[]),
]
