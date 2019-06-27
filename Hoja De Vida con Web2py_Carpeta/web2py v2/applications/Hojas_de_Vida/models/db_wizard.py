### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_hoja_vida',
    Field('f_nombre', type='string', notnull=True,
          label=T('Nombre')),
    Field('f_foto', 'upload'),
    Field('f_telefono', type='string', notnull=True,
          label=T('Telefono')),
    Field('f_direccion', type='string', notnull=True,
          label=T('Direccion')),
    Field('f_documento', type='string', notnull=True, unique=False,
          label=T('Documento')),
    Field('f_fecha_nacimiento', type='date', notnull=True,
          label=T('Fecha Nacimiento')),
    Field('f_perfil', type='string',
          label=T('Perfil')),
    auth.signature,
    format='%(f_nombre)s',
    migrate=settings.migrate)

db.define_table('t_hoja_vida_archive',db.t_hoja_vida,Field('current_record','reference t_hoja_vida',readable=False,writable=False))

########################################
db.define_table('t_tipo_estudio',
    Field('f_nombre', type='string', notnull=True,
          label=T('Nombre')),
    auth.signature,
    format='%(f_nombre)s',
    migrate=settings.migrate)

db.define_table('t_tipo_estudio_archive',db.t_tipo_estudio,Field('current_record','reference t_tipo_estudio',readable=False,writable=False))

########################################
db.define_table('t_experiencia_laboral',
    Field('f_empresa', type='string', notnull=True,
          label=T('Empresa')),
    Field('f_cargo', type='string', notnull=True,
          label=T('Cargo')),
    Field('f_fecha_inicio', type='date', notnull=True,
          label=T('Fecha Inicio')),
    Field('f_fecha_fin', type='date',
          label=T('Fecha Fin')),
    Field('f_hoja', type='reference t_hoja_vida', notnull=True,
          label=T('Hoja')),
    auth.signature,
    format='%(f_empresa)s',
    migrate=settings.migrate)

db.define_table('t_experiencia_laboral_archive',db.t_experiencia_laboral,Field('current_record','reference t_experiencia_laboral',readable=False,writable=False))

########################################
db.define_table('t_formacion_academica',
    Field('f_institucion', type='string', notnull=True,
          label=T('Institucion')),
    Field('f_fecha_inicio', type='date', notnull=True,
          label=T('Fecha Inicio')),
    Field('f_fecha_fin', type='date',
          label=T('Fecha Fin')),
    Field('f_tipo', type='reference t_tipo_estudio', notnull=True,
          label=T('Tipo')),
    Field('f_hoja', type='reference t_hoja_vida', notnull=True,
          label=T('Hoja')),
    Field('f_titulo', type='string', notnull=True,
          label=T('Titulo')),
    auth.signature,
    format='%(f_institucion)s',
    migrate=settings.migrate)

db.define_table('t_formacion_academica_archive',db.t_formacion_academica,Field('current_record','reference t_formacion_academica',readable=False,writable=False))
