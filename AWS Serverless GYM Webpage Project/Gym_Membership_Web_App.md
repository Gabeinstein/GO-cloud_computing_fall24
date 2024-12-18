# Aplicación Web para Membresías de Gimnasio

Este proyecto es una aplicación web alojada en la nube y diseñada para un gimnasio, desplegada en AWS. La página muestra las membresías del gimnasio de forma dinámica, obtenidas a través de una REST API conectada a una base de datos. Los usuarios pueden alternar entre ver todas las membresías o solo aquellas marcadas como "populares". Además, incluye una funcionalidad de inicio de sesión que permite a los usuarios autenticarse y visualizar las membresías a las que están suscritos, ofreciendo una experiencia personalizada.

El despliegue se automatiza mediante un script `setup.sh`, que utiliza AWS CLI y SDK para configurar rápidamente la aplicación en la nube. Esta solución facilita la gestión de membresías de forma escalable y eficiente.

## Estructura del Proyecto

El proyecto contiene un directorio `/resources/setup.sh`, que incluye todos los comandos necesarios para la generación y habilitación de los diferentes servicios utilizados en nuestro proyecto.

## Configuraciones Manuales

Las únicas configuraciones realizadas manualmente fueron:
- La configuración de CORS en los diferentes API Gateways generados.

---

Este enfoque asegura una implementación ágil y adaptable para la gestión de membresías en gimnasios modernos.
