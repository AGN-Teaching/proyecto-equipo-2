[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/XixB-tii)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=12217425)
Informe sobre el Sistema de Streaming de Música
Introducción
El presente informe se centra en el diseño y desarrollo de un sistema de streaming de música, una plataforma que permite a los usuarios acceder y disfrutar de música en línea. Este proyecto aborda diversos aspectos, desde la gestión de cuentas de usuario hasta la reproducción de canciones y la creación de listas de reproducción personalizadas. A lo largo de este informe, analizaremos en profundidad el problema que intentamos resolver, presentaremos las conclusiones derivadas de nuestro análisis, describiremos en detalle el diseño de la solución, explicaremos cómo funciona el sistema y, finalmente, exploraremos las clases involucradas, sus relaciones y posibles mejoras.

Análisis del Problema
El problema central al que nos enfrentamos es la creación de un sistema de streaming de música que ofrezca una experiencia completa y atractiva a los usuarios. Esto implica resolver los siguientes desafíos:
Gestión de Usuarios y Cuentas: Los usuarios deben poder registrarse, iniciar sesión y acceder a sus cuentas de usuario. También deben poder elegir entre diferentes planes de suscripción.
Catálogo de Música: El sistema debe contener un catálogo de canciones con información detallada, como título, artista y álbum. Los usuarios deben poder buscar y acceder a estas canciones.
Reproducción de Canciones: Los usuarios deben poder reproducir canciones y, en función de su plan de suscripción, pueden estar sujetos a anuncios publicitarios.
Listas de Reproducción Personalizadas: Los usuarios deben poder crear y gestionar sus propias listas de reproducción con canciones de su elección.

Diseño de la Solución
La solución propuesta se basa en una arquitectura orientada a objetos y consta de las siguientes clases principales:

Clase Streaming:
Descripción: Esta clase es el corazón del sistema y coordina todas las operaciones. Gestiona clientes, el catálogo de música y la reproducción de canciones.
Métodos y Funciones: Incluye métodos para crear cuentas de usuario, cargar el catálogo de canciones desde un archivo JSON y reproducir canciones.

Clase Cliente:
Descripción: Representa a los usuarios y sus planes de suscripción. Cada cliente puede tener múltiples cuentas.
Métodos y Funciones: Permite la creación de cuentas y la gestión de planes de suscripción.

Clase Cuenta:
Descripción: Representa una cuenta de usuario individual y almacena información sobre las listas de reproducción, los anuncios y el plan de suscripción.
Métodos y Funciones: Gestiona la creación de listas de reproducción, la reproducción de canciones y la gestión de anuncios.

Clase Canción:
Descripción: Representa una canción en el catálogo de música. Contiene detalles como título, artista y álbum.
Métodos y Funciones: Facilita la búsqueda de canciones y su reproducción.

Gestión de Anuncios:
Descripción: Los anuncios se gestionan a través de la clase Streaming y se muestran a los usuarios en función de su plan de suscripción.

Listas de Reproducción:
Descripción: Las listas de reproducción se gestionan a través de la clase Cuenta. Los usuarios pueden crear, editar y reproducir listas de reproducción personalizadas.



Funcionamiento e Implementación
El sistema opera de la siguiente manera:
Un usuario accede al sistema y puede elegir entre contratar un plan de suscripción o acceder a uno existente.
Para contratar un plan, el usuario proporciona su nombre y elige el tipo de plan (Gratuito, Individual, Estudiantes, Familiar).
Cuando un cliente accede a su plan existente, el sistema verifica su nombre y recupera la instancia de Cliente correspondiente.
Los usuarios pueden crear cuentas de usuario individuales con nombres únicos y relacionados con su cliente.
El catálogo de canciones se carga desde un archivo JSON y se almacena en la clase Streaming.
Los usuarios pueden buscar canciones por título, artista o álbum, lo que implica una búsqueda en el catálogo de canciones.
La reproducción de canciones se realiza a través de un reproductor y muestra anuncios si el plan del usuario lo permite.
Los usuarios pueden crear listas de reproducción personalizadas y agregar canciones a ellas.

Descripción y Análisis de las Clases
Cada clase cumple un papel fundamental en el funcionamiento del sistema:
La clase Streaming coordina todas las operaciones y gestiona las relaciones entre los clientes, las cuentas, el catálogo y la reproducción.
La clase Cliente permite la gestión de usuarios y sus planes de suscripción, lo que influye en la disponibilidad de anuncios.
La clase Cuenta administra las cuentas de usuario individuales y las listas de reproducción personalizadas, lo que ofrece una experiencia única a cada usuario.
La clase Canción es esencial para el catálogo de música, permitiendo la búsqueda y reproducción de canciones.



Posibles Mejoras
A pesar de la robustez de la solución propuesta, existen áreas que podrían mejorarse:
Seguridad: La implementación actual no aborda la autenticación de usuarios ni la protección de datos sensibles. Mejorar la seguridad es fundamental.

Escalabilidad: Con un crecimiento significativo de usuarios y canciones, la arquitectura actual podría volverse ineficiente. Una optimización para la escalabilidad es esencial.

Recomendaciones de Música: La incorporación de algoritmos de recomendación podría mejorar la experiencia del usuario.

Justificación de Relaciones entre Clases
Las relaciones entre las clases están diseñadas para representar de manera efectiva la interacción entre los componentes del sistema. Por ejemplo, la clase Cliente actúa como un "contenedor" para las cuentas de usuario individuales, lo que refleja la relación de "uno a muchos". La clase Cuenta se relaciona con la clase Canción para permitir la creación de listas de reproducción personalizadas. La clase Streaming coordina todas las operaciones y actúa como el "centro de mando" del sistema.
Conclusiones
Tras un análisis exhaustivo de los desafíos y requisitos, hemos llegado a las siguientes conclusiones:
La gestión de cuentas de usuario es esencial para personalizar la experiencia de cada usuario y administrar sus preferencias.El catálogo de música debe estar bien organizado y permitir una búsqueda eficiente de canciones.
La reproducción de canciones debe ser fluida y puede requerir la gestión de anuncios.Las listas de reproducción personalizadas permiten a los usuarios crear su propia experiencia musical.
El sistema de streaming de música desarrollado ofrece una solución completa y eficiente para permitir a los usuarios acceder y disfrutar de música en línea. A través de una gestión de cuentas, un catálogo de música organizado, la reproducción de canciones y la creación de listas de reproducción, se abordan los principales desafíos y requisitos del proyecto. Además, las posibles mejoras identificadas permiten un camino claro para futuras actualizaciones y expansiones.

El sistema, basado en una arquitectura orientada a objetos, proporciona una base sólida para brindar una experiencia musical atractiva y personalizada a los usuarios. Sin embargo, se recomienda encarecidamente mejorar la seguridad y abordar la escalabilidad para garantizar un funcionamiento óptimo a medida que el sistema crece. Además, la implementación de recomendaciones de música podría llevar la experiencia del usuario a un nivel superior.

