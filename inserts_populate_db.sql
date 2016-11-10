-- Patrones
INSERT INTO  PatronPedagogico  VALUES (1, 'Early bird', '01');
INSERT INTO  PatronPedagogico  VALUES (2, 'Spiral', '02');
INSERT INTO  PatronPedagogico  VALUES (3, 'Lay of the land', '03');
INSERT INTO  PatronPedagogico  VALUES (4, 'Toy box', '04');
INSERT INTO  PatronPedagogico  VALUES (5, 'Toolbox', '05');
INSERT INTO  PatronPedagogico  VALUES (6, 'Sin patrón', '06');

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
INSERT INTO  SeccionNombre  VALUES (19, 'Contenido', 6);

-- TipoUsuario
insert into TipoUsuario values (1, 'Administrador', now(), now());
insert into TipoUsuario values (2, 'Docente editor', now(), now());
insert into TipoUsuario values (3, 'Docente', now(), now());

-- Menu
INSERT INTO Menu VALUES (1,'Menu Administrador','index_administrador',now(), now());
INSERT INTO Menu VALUES (2,'Listado usuarios','usuarios_index',now(), now());
INSERT INTO Menu VALUES (3,'Edición usuario','usuarios_edit',now(), now());
INSERT INTO Menu VALUES (4,'Listado perfiles','perfiles_index',now(), now());	 
INSERT INTO Menu VALUES (5,'Edición perfiles', 'perfiles_edit', now(), now());			 
INSERT INTO Menu VALUES (6,'Usuario base','index_usuarioBase', now(), now());
INSERT INTO Menu VALUES (7,'Crear objeto','CrearOA', now(), now());
INSERT INTO Menu VALUES (8,'Edición OA', 'EditarOA', now(), now());

-- MenuTipoUsuario
INSERT INTO MenuTipoUsuario VALUES (1, 1, 1);
INSERT INTO MenuTipoUsuario VALUES (2, 2, 1);
INSERT INTO MenuTipoUsuario VALUES (3, 3, 1);
INSERT INTO MenuTipoUsuario VALUES (4, 4, 1);	 
INSERT INTO MenuTipoUsuario VALUES (5, 5, 1);
INSERT INTO MenuTipoUsuario VALUES (6, 6, 1);
INSERT INTO MenuTipoUsuario VALUES (7, 6, 2);
INSERT INTO MenuTipoUsuario VALUES (8, 6, 3);
INSERT INTO MenuTipoUsuario VALUES (9, 7, 1);
INSERT INTO MenuTipoUsuario VALUES (10, 7, 2);
INSERT INTO MenuTipoUsuario VALUES (11, 8, 1);
INSERT INTO MenuTipoUsuario VALUES (12, 8, 2);
-- TEST INSERT INTO MenuTipoUsuario VALUES (13, 7, 3);
-- TEST INSERT INTO MenuTipoUsuario VALUES (14, 8, 3);


-- Usuario administrador
INSERT INTO Usuario VALUES (1, 'Marcos', 'Amaro', '31332463', 'Sistemas', 'pbkdf2_sha256$10000$tVOHTWJkvxWi$MUIwLvb+A+Xtmm3z8Ux04AEMz+WLtLbUyMpCrWac9qs=','marcos.n.amaro@gmail.com',TRUE,'2016-10-20 03:38:55.0','2016-10-25 03:51:35.0', TRUE, 1);

-- Docente editor
INSERT INTO Usuario VALUES (2, 'Carlos', 'García', '12345678', 'Nutrición', 'pbkdf2_sha256$10000$tVOHTWJkvxWi$MUIwLvb+A+Xtmm3z8Ux04AEMz+WLtLbUyMpCrWac9qs=','marcos.amaro@ymail.com',TRUE,'2016-10-20 03:38:55.0','2016-10-25 03:51:35.0', TRUE, 2);

-- Docente
INSERT INTO Usuario VALUES (3, 'Micaela', 'Gonzalez', '12345679', 'Audiovisión', 'pbkdf2_sha256$10000$tVOHTWJkvxWi$MUIwLvb+A+Xtmm3z8Ux04AEMz+WLtLbUyMpCrWac9qs=','adoa2.unla@gmail.com',TRUE,'2016-10-20 03:38:55.0','2016-10-25 03:51:35.0', FALSE, 3);

COMMIT;
