-- Patrones
INSERT INTO  PatronPedagogico  VALUES (1, 'Early bird', '01');
INSERT INTO  PatronPedagogico  VALUES (2, 'Spiral', '02');
INSERT INTO  PatronPedagogico  VALUES (3, 'Lay of the land', '03');
INSERT INTO  PatronPedagogico  VALUES (4, 'Toy box', '04');
INSERT INTO  PatronPedagogico  VALUES (5, 'Toolbox', '05');

-- Secciones
INSERT INTO  SeccionNombre  VALUES (1, 'Ideas principales', 1);
INSERT INTO  SeccionNombre  VALUES (2, 'Desarrollo', 1);
INSERT INTO  SeccionNombre  VALUES (3, 'Primera aproximación', 2);
INSERT INTO  SeccionNombre  VALUES (4, 'Idea general', 2);
INSERT INTO  SeccionNombre  VALUES (5, 'Detalles', 2);
INSERT INTO  SeccionNombre  VALUES (6, 'Conclusión', 2);
INSERT INTO  SeccionNombre  VALUES (7, 'Presentación del tema', 3);
INSERT INTO  SeccionNombre  VALUES (8, 'Explicación de un caso', 3);
INSERT INTO  SeccionNombre  VALUES (9, 'Detección de errores', 3);
INSERT INTO  SeccionNombre  VALUES (10, 'Detección de aciertos', 3);
INSERT INTO  SeccionNombre  VALUES (11, 'Explicación de un caso', 4);
INSERT INTO  SeccionNombre  VALUES (12, 'Métodos de resolución alternativos', 4);
INSERT INTO  SeccionNombre  VALUES (13, 'Primeras aplicaciones de los métodos', 4);
INSERT INTO  SeccionNombre  VALUES (14, 'Transición a la actualidad', 4);
INSERT INTO  SeccionNombre  VALUES (15, 'Situación actual de la problemática', 5);
INSERT INTO  SeccionNombre  VALUES (16, 'Síntesis de herramientas', 5);
INSERT INTO  SeccionNombre  VALUES (17, 'Explicación metodología 1', 5);
INSERT INTO  SeccionNombre  VALUES (18, 'Explicación metodología 2', 5);

-- TipoUsuario
insert into TipoUsuario values (1, 'Administrador', now(), now());
insert into TipoUsuario values (2, 'Docente editor', now(), now());
insert into TipoUsuario values (3, 'Docente común', now(), now());

-- Menu
INSERT INTO `Menu`(id,
                   nombre,
                   url,
                   created,
                   updated)
     VALUES (1,
             'Menu Administrador',
             'index_administrador',
             '2016-10-20 01:24:38.0',
             '2016-10-20 01:24:38.0');

INSERT INTO `Menu`(id,
                   nombre,
                   url,
                   created,
                   updated)
     VALUES (2,
             'Listado usuarios',
             'usuarios_index',
             '2016-10-20 03:14:29.0',
             '2016-10-20 03:14:29.0');

INSERT INTO `Menu`(id,
                   nombre,
                   url,
                   created,
                   updated)
     VALUES (3,
             'Edición usuario',
             'usuarios_edit',
             '2016-10-20 03:16:44.0',
             '2016-10-20 03:16:44.0');

INSERT INTO `Menu`(id,
                   nombre,
                   url,
                   created,
                   updated)
     VALUES (4,
             'Listado perfiles',
             'perfiles_index',
             '2016-10-20 03:19:03.0',
             '2016-10-20 03:19:03.0');   
             
-- MenuTipoUsuarios
INSERT INTO usuario_menu_tipousuarios(id, menu_id, tipousuario_id)
     VALUES (1, 1, 1);

INSERT INTO usuario_menu_tipousuarios(id, menu_id, tipousuario_id)
     VALUES (2, 2, 1);

INSERT INTO usuario_menu_tipousuarios(id, menu_id, tipousuario_id)
     VALUES (3, 3, 1);

INSERT INTO usuario_menu_tipousuarios(id, menu_id, tipousuario_id)
     VALUES (4, 4, 1);   
     
COMMIT;
