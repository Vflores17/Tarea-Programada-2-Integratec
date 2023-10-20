import requests
from bs4 import BeautifulSoup
import random
from faker import Faker
import re
import datetime
import csv

urlSedes="https://www.tec.ac.cr/carreras"
totalAdmitidos={"CTLSC":175,"CTLSJ":75,"CAL":75,"CTCC":625,"CAA":50}
estructura={'CTLSC': [['Bachillerato en Administración de Empresas', 25], ['Bachillerato en Gestión del Turismo Rural Sostenible', 25], ['Bachillerato en Gestión en Sostenibilidad Turística', 25], ['Bachillerato en Ingeniería en Computación', 25], ['Licenciatura en Ingeniería Electrónica', 25], ['Licenciatura en Ingeniería en Agronomía', 25], ['Licenciatura en Ingeniería en Producción Industrial', 25]], 'CTLSJ': [['Bachillerato en Administración de Empresas', 25], ['Bachillerato en Ingeniería en Computación', 25], ['Licenciatura en Arquitectura', 25]], 'CAL': [['Bachillerato en Administración de Empresas', 25], ['Bachillerato en Ingeniería en Computación', 25], ['Bachillerato en Producción Industrial,  Limón', 25]], 'CTCC': [['Bachillerato en Administración de Empresas', 25], ['Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 25], ['Bachillerato en Gestión del Turismo Sostenible', 25], ['Bachillerato en Ingeniería en Biotecnología', 25], ['Bachillerato en Ingeniería en Computación', 25], ['Licenciatura en Administración de Tecnología de Información', 25], ['Licenciatura en Ingeniería Agrícola', 25], ['Licenciatura en Ingeniería Ambiental', 25], ['Licenciatura en Ingeniería Electrónica', 25], ['Licenciatura en Ingeniería en Agronegocios', 25], ['Licenciatura en Ingeniería en Computadores', 25], ['Licenciatura en Ingeniería en Construcción', 25], ['Licenciatura en Ingeniería en Diseño Industrial', 25], ['Licenciatura en Ingeniería en Materiales', 25], ['Licenciatura en Ingeniería en Producción Industrial', 25], ['Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 25], ['Licenciatura en Ingeniería Física', 25], ['Licenciatura en Ingeniería Forestal', 25], ['Licenciatura en Ingeniería Mecatrónica', 25], ['Licenciatura en Mantenimiento Industrial', 25]], 'CAA': [['Bachillerato en Ingeniería en Computación', 25], ['Licenciatura en Ingeniería Electrónica', 25]]}
diccEstudiantes={' 2024025746 ': [('Heather', 'Harris', 'Carroll'), 64143356, 'HeHarris@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,

' 2024023376 ': [('Joseph', 'Gibbs', 'Davis'), 80543506, 'JoGibbs@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024029231 ': [('Carl', 'Wolfe', 'Nelson'), 97530014, 'CaWolfe@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024029621 ': [('Robert', 'Simpson', 'Singleton'), 78175530, 'RoSimpson@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024023035 ': [('Ashley', 'Thomas', 'Merritt'), 95299943, 'AsThomas@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024025433 ': [('James', 'Hernandez', 'Clark'), 96488318, 'JaHernandez@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024022841 ': [('Kathryn', 'Alexander', 'Stout'), 88762951, 'KaAlexander@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024024527 ': [('Kathryn', 'Davenport', 'Oconnor'), 96682808, 'KaDavenport@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024026257 ': [('Kelly', 'Eaton', 'Lee'), 78207470, 'KeEaton@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024028627 ': [('Sarah', 'Marshall', 'Davis'), 97564773, 'SaMarshall@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024023889 ': [('Benjamin', 'Johnson', 'Franco'), 80380693, 'BeJohnson@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024024787 ': [('John', 'Gomez', 'Bishop'), 82075133, 'JoGomez@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024025795 ': [('Shannon', 'Gallegos', 'Murphy'), 60930965, 'ShGallegos@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024022539 ': [('Denise', 'Marshall', 'Pugh'), 94459542, 'DeMarshall@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024029292 ': [('Shawn', 'Kim', 'Obrien'), 69092040, 'ShKim@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024029784 ': [('Cynthia', 'Rogers', 'Crawford'), 94740121, 'CyRogers@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024028218 ': [('David', 'Ramirez', 'Gordon'), 63722984, 'DaRamirez@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024023596 ': [('Martin', 'Harrell', 'Oconnell'), 61064483, 'MaHarrell@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024021895 ': [('Angel', 'Herrera', 'Murphy'), 89883028, 'AnHerrera@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024023564 ': [('Lori', 'Hernandez', 'Black'), 79341655, 'LoHernandez@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024028731 ': [('Beth', 'Flores', 'Collins'), 82067956, 'BeFlores@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024027853 ': [('Herbert', 'Hernandez', 'Smith'), 98858222, 'HeHernandez@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024024316 ': [('Stephen', 'Gonzalez', 'Tucker'), 78901960, 'StGonzalez@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024021203 ': [('Vincent', 'Sanchez', 'Burton'), 93139024, 'ViSanchez@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024022636 ': [('Brian', 'Randolph', 'Mejia'), 93752436, 'BrRandolph@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024029670 ': [('Nicholas', 'Edwards', 'Gentry'), 63469432, 'NiEdwards@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024026323 ': [('Crystal', 'Edwards', 'Matthews'), 81867357, 'CrEdwards@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024022607 ': [('Megan', 'Long', 'Green'), 90239417, 'MeLong@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024028182 ': [('Colleen', 'Rojas', 'Jones'), 66634589, 'CoRojas@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024023094 ': [('Brian', 'Gilmore', 'Villarreal'), 68626849, 'BrGilmore@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024022107 ': [('Brianna', 'Livingston', 'Page'), 82080521, 'BrLivingston@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024028349 ': [('Matthew', 'Simmons', 'Carroll'), 88166453, 'MaSimmons@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024028362 ': [('Tammie', 'House', 'Bonilla'), 84242731, 'TaHouse@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024021048 ': [('Amy', 'Navarro', 'Thomas'), 72877229, 'AmNavarro@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024021535 ': [('Lisa', 'York', 'Pham'), 77538450, 'LiYork@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024025983 ': [('Joshua', 'Clark', 'Willis'), 78115099, 'JoClark@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024025596 ': [('Suzanne', 'Grant', 'Hernandez'), 64956626, 'SuGrant@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024025275 ': [('Jesse', 'Dominguez', 'Wilson'), 81944190, 'JeDominguez@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024026246 ': [('James', 'Allen', 'Wood'), 96660272, 'JaAllen@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024027739 ': [('Larry', 'Brown', 'Nunez'), 62652910, 'LaBrown@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024022508 ': [('Erica', 'Gonzalez', 'Ward'), 67203445, 'ErGonzalez@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024021730 ': [('Justin', 'Daniels', 'Brewer'), 78411458, 'JuDaniels@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024021043 ': [('Harold', 'Roberts', 'Rodgers'), 81010898, 'HaRoberts@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024023064 ': [('Joseph', 'Johnson', 'Cross'), 90748901, 'JoJohnson@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024029842 ': [('Tracy', 'Richards', 'Bradley'), 80694058, 'TrRichards@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024023156 ': [('Jared', 'Brown', 'Atkinson'), 78034054, 'JaBrown@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024027934 ': [('Patricia', 'Bowen', 'Pace'), 82728380, 'PaBowen@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024021880 ': [('Debra', 'Velez', 'Griffin'), 82308360, 'DeVelez@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024027222 ': [('Jamie', 'Carpenter', 'Howard'), 61642965, 'JaCarpenter@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024021083 ': [('Samuel', 'Ramirez', 'Osborne'), 70136643, 'SaRamirez@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0] ,
' 2024021090 ': [('Heather', 'Evans', 'Bishop'), 76502600, 'HeEvans@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024023318 ': [('Richard', 'Patel', 'Wilson'), 61275614, 'RiPatel@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024027633 ': [('Rebecca', 'Keller', 'Roth'), 89298287, 'ReKeller@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024023826 ': [('Danielle', 'Alexander', 'Christensen'), 88552361, 'DaAlexander@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024027768 ': [('Jeffrey', 'Solis', 'Greene'), 60269703, 'JeSolis@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024028165 ': [('Tony', 'Calderon', 'Gilmore'), 98117765, 'ToCalderon@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024022798 ': [('Justin', 'Williams', 'Gonzalez'), 78999407, 'JuWilliams@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024027063 ': [('Trevor', 'Kidd', 'Savage'), 66070312, 'TrKidd@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024021712 ': [('Nathan', 'Edwards', 'Lopez'), 79897053, 'NaEdwards@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024027243 ': [('Jasmine', 'Jackson', 'Torres'), 87103935, 'JaJackson@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024024877 ': [('Brittany', 'Wheeler', 'Smith'), 87251434, 'BrWheeler@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024022505 ': [('Meredith', 'Hall', 'Murphy'), 75252776, 'MeHall@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024021799 ': [('Angela', 'Young', 'Lee'), 67686397, 'AnYoung@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024027376 ': [('Juan', 'Mathis', 'Brooks'), 86047625, 'JuMathis@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024028141 ': [('Elizabeth', 'Fox', 'Harper'), 60043613, 'ElFox@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024025126 ': [('Cindy', 'Gardner', 'Mccormick'), 87630243, 'CiGardner@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024022153 ': [('Pamela', 'Mcclure', 'Molina'), 77927213, 'PaMcclure@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024029162 ': [('Alexis', 'Fox', 'Hall'), 66088898, 'AlFox@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024029814 ': [('Melissa', 'Walters', 'Villegas'), 65332380, 'MeWalters@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024026702 ': [('Lisa', 'Johnson', 'Barker'), 72839006, 'LiJohnson@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024027127 ': [('William', 'Lee', 'Schwartz'), 75707163, 'WiLee@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024024035 ': [('Sherri', 'Shepherd', 'Harris'), 73320443, 'ShShepherd@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024022359 ': [('Abigail', 'Anderson', 'Ramirez'), 85822907, 'AbAnderson@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024029472 ': [('Summer', 'Harris', 'Roberts'), 85667385, 'SuHarris@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024027171 ': [('Charles', 'York', 'Hines'), 85790677, 'ChYork@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0] ,
' 2024021492 ': [('Sabrina', 'Strong', 'Kennedy'), 65153914, 'SaStrong@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024021677 ': [('Michael', 'Espinoza', 'Pratt'), 62601257, 'MiEspinoza@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024028820 ': [('Edward', 'Le', 'Hodges'), 60131822, 'EdLe@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024021523 ': [('Stephen', 'Keller', 'Salazar'), 92993558, 'StKeller@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024028077 ': [('Karen', 'Deleon', 'Oneill'), 83669871, 'KaDeleon@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024025252 ': [('Billy', 'Leon', 'Allison'), 70839107, 'BiLeon@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024025061 ': [('Eileen', 'Baker', 'Robles'), 98140409, 'EiBaker@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024023466 ': [('Austin', 'Padilla', 'Cain'), 77230635, 'AuPadilla@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024026601 ': [('Megan', 'Bradley', 'Wilson'), 78004806, 'MeBradley@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024025092 ': [('Amanda', 'Thomas', 'Fisher'), 96326864, 'AmThomas@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024029679 ': [('Jamie', 'Snyder', 'Richard'), 75297593, 'JaSnyder@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024026827 ': [('Diana', 'Rodriguez', 'Irwin'), 88810080, 'DiRodriguez@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024027043 ': [('Tina', 'Watkins', 'Case'), 69384036, 'TiWatkins@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024025455 ': [('Gregory', 'Cruz', 'Gutierrez'), 90314906, 'GrCruz@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024021803 ': [('Kimberly', 'Farrell', 'Owen'), 93874487, 'KiFarrell@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024022975 ': [('Jonathan', 'Ramirez', 'Anderson'), 68885948, 'JoRamirez@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024029501 ': [('Jamie', 'Hernandez', 'Banks'), 92326759, 'JamHernandez6@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024024144 ': [('Mitchell', 'Reeves', 'Turner'), 88156927, 'MiReeves@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024023584 ': [('Elizabeth', 'Wood', 'Thompson'), 97062557, 'ElWood@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024027261 ': [('Marcus', 'Bautista', 'Gordon'), 66851798, 'MaBautista@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024024305 ': [('Tim', 'Schneider', 'Huynh'), 83103317, 'TiSchneider@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024025286 ': [('Jodi', 'Moore', 'Brown'), 90899353, 'JoMoore@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024021136 ': [('John', 'Reed', 'Allen'), 77175152, 'JoReed@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024026877 ': [('Justin', 'Rosales', 'Hull'), 76036925, 'JuRosales@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024021415 ': [('Dawn', 'Jones', 'Smith'), 99907941, 'DaJones@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024023435 ': [('Christopher', 'Rodriguez', 'Cook'), 78082796, 'ChRodriguez@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024026840 ': [('Austin', 'Taylor', 'Davidson'), 90225626, 'AuTaylor@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024026796 ': [('Amy', 'Peck', 'Nash'), 60050532, 'AmPeck@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024022699 ': [('Jonathan', 'Bell', 'Martin'), 96234410, 'JoBell@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024028859 ': [('Matthew', 'Lopez', 'Wilson'), 72468450, 'MaLopez@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024029030 ': [('Dana', 'Norton', 'Sanchez'), 73120482, 'DaNorton@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024028097 ': [('Brandy', 'Welch', 'Espinoza'), 82872730, 'BrWelch@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024026117 ': [('Lacey', 'Orr', 'Meyer'), 62236561, 'LaOrr@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024029458 ': [('Adam', 'Thompson', 'Jenkins'), 72213681, 'AdThompson@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024022306 ': [('Christopher', 'Price', 'Smith'), 82709798, 'ChPrice@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024028121 ': [('Matthew', 'Hoffman', 'Torres'), 65383349, 'MaHoffman@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024024310 ': [('Christopher', 'Cunningham', 'Williams'), 82700822, 'ChCunningham@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024028885 ': [('Brandi', 'Morgan', 'Bird'), 99586736, 'BrMorgan@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024022128 ': [('Stephen', 'Nguyen', 'Fletcher'), 68504275, 'StNguyen@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024026154 ': [('Matthew', 'Wheeler', 'Robinson'), 98173026, 'MaWheeler@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024021367 ': [('William', 'Lawrence', 'Sims'), 73193227, 'WiLawrence@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024021936 ': [('Barbara', 'Campos', 'Miller'), 95843802, 'BaCampos@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024026427 ': [('Christopher', 'Williams', 'Campbell'), 89096357, 'ChWilliams@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024022334 ': [('Sara', 'Phillips', 'Miller'), 86514464, 'SaPhillips@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024022483 ': [('Edwin', 'Ramirez', 'Riley'), 86335273, 'EdRamirez@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024022715 ': [('Matthew', 'Murphy', 'Alvarez'), 61040849, 'MaMurphy@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024026399 ': [('Danielle', 'Washington', 'Castillo'), 95675242, 'DaWashington@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024022889 ': [('Julia', 'Williams', 'Woods'), 69355369, 'JulWilliams9@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024021134 ': [('Kristen', 'Shea', 'Holland'), 78384827, 'KrShea@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024028635 ': [('Christopher', 'King', 'Kidd'), 67113962, 'ChKing@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024024456 ': [('Anthony', 'Pennington', 'Morris'), 94938261, 'AnPennington@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024022787 ': [('William', 'Mayer', 'Lloyd'), 89907296, 'WiMayer@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024028379 ': [('Marissa', 'Lee', 'Gibson'), 70396258, 'MaLee@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024023981 ': [('Anita', 'Jackson', 'Ware'), 81014691, 'AnJackson@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024028691 ': [('Austin', 'Wilson', 'Shelton'), 85114886, 'AuWilson@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024025386 ': [('Kathleen', 'Lambert', 'Shaw'), 83757976, 'KaLambert@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024025656 ': [('Angela', 'Herman', 'Branch'), 78277516, 'AnHerman@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024021623 ': [('Daniel', 'Bond', 'Pratt'), 79879065, 'DaBond@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024026783 ': [('Drew', 'Case', 'White'), 85873068, 'DrCase@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024021288 ': [('Ricky', 'Solomon', 'Graham'), 85073279, 'RiSolomon@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024021140 ': [('Darlene', 'Morales', 'Turner'), 82450378, 'DaMorales@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024029841 ': [('Samuel', 'Jones', 'Brown'), 83084350, 'SaJones@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024026146 ': [('Gary', 'Ortega', 'Jackson'), 78051746, 'GaOrtega@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024024394 ': [('William', 'Hayes', 'Smith'), 82802672, 'WiHayes@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024023774 ': [('Samantha', 'Vance', 'Johnson'), 99203462, 'SaVance@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024026999 ': [('Cheryl', 'Hudson', 'Hanson'), 81667323, 'ChHudson@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024027453 ': [('Jacob', 'Mendoza', 'Huerta'), 86526555, 'JaMendoza@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024026519 ': [('Michael', 'Allison', 'Richardson'), 67174386, 'MiAllison@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024023517 ': [('Stephen', 'Oconnell', 'Hatfield'), 64806021, 'StOconnell@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024022337 ': [('Kevin', 'Harrison', 'Armstrong'), 61624272, 'KeHarrison@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024025335 ': [('Christine', 'Walter', 'Taylor'), 98379399, 'ChWalter@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024026888 ': [('Angel', 'Sutton', 'Morrison'), 74433290, 'AnSutton@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024027515 ': [('Cheryl', 'Bender', 'Quinn'), 88742257, 'ChBender@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024028727 ': [('David', 'Powell', 'Wilcox'), 92379789, 'DaPowell@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024026138 ': [('Stanley', 'Kent', 'Simmons'), 99683018, 'StKent@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Agronomía', 0] ,
' 2024023437 ': [('Tony', 'Roberson', 'Little'), 93698497, 'ToRoberson@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024021398 ': [('Todd', 'Perry', 'Harris'), 70888599, 'ToPerry@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024023246 ': [('Blake', 'Griffin', 'Bradley'), 91219883, 'BlGriffin@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024022362 ': [('Joshua', 'Randall', 'Cobb'), 80081254, 'JoRandall@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024024795 ': [('Nicholas', 'Peters', 'Oneill'), 60731340, 'NiPeters@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024029323 ': [('Thomas', 'Schwartz', 'Thomas'), 85772499, 'ThSchwartz@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024023117 ': [('Marcus', 'Baker', 'Miller'), 69630099, 'MaBaker@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024029377 ': [('Nathan', 'Palmer', 'Hanson'), 78685776, 'NaPalmer@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024021930 ': [('Jared', 'Madden', 'Cantrell'), 86482684, 'JaMadden@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024024551 ': [('Christine', 'Thomas', 'Kramer'), 87671530, 'ChThomas@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024027477 ': [('Krista', 'Baker', 'Haley'), 71437262, 'KrBaker@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024025941 ': [('Kevin', 'Huber', 'Cardenas'), 76545412, 'KeHuber@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024028390 ': [('Shawn', 'Jackson', 'Smith'), 90450894, 'ShJackson@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024021816 ': [('Kirk', 'Webb', 'Graves'), 94054766, 'KiWebb@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024026648 ': [('Teresa', 'Gilbert', 'Lopez'), 80158938, 'TeGilbert@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024028673 ': [('Paula', 'Rivas', 'Krueger'), 71187572, 'PaRivas@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024028720 ': [('Diana', 'Bell', 'Rodriguez'), 78332717, 'DiBell@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024021997 ': [('Jeff', 'Dickerson', 'Lawson'), 78481657, 'JeDickerson@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024028089 ': [('David', 'Marquez', 'Gibson'), 96261352, 'DaMarquez@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024021883 ': [('Matthew', 'Rodriguez', 'Reed'), 82697757, 'MaRodriguez@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024029300 ': [('Mark', 'Powell', 'Odom'), 79101264, 'MaPowell@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024029813 ': [('Richard', 'Medina', 'Snyder'), 79027559, 'RiMedina@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024024617 ': [('Debbie', 'Phillips', 'Henderson'), 97064358, 'DePhillips@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024022844 ': [('Crystal', 'Brown', 'Sandoval'), 85708178, 'CrBrown@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024026855 ': [('Mary', 'Davidson', 'Garcia'), 86068354, 'MaDavidson@estudiantec.cr', 'CTLSC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024032319 ': [('Meghan', 'Watkins', 'Morris'), 62659644, 'MeWatkins@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024037057 ': [('Donald', 'Silva', 'Williams'), 68988716, 'DoSilva@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024034271 ': [('Jessica', 'Johnson', 'Cunningham'), 62390305, 'JeJohnson@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024037765 ': [('Julie', 'Allen', 'Booth'), 66770874, 'JuAllen@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024033195 ': [('Claire', 'Green', 'Bowers'), 62055014, 'ClGreen@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024031768 ': [('Dennis', 'Miles', 'Orr'), 86484587, 'DeMiles@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024031850 ': [('Ryan', 'Burns', 'Robertson'), 76542391, 'RyBurns@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024032749 ': [('John', 'White', 'Martin'), 78174409, 'JoWhite@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024036096 ': [('Amber', 'Rodriguez', 'Lloyd'), 81422519, 'AmRodriguez@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024039560 ': [('Robert', 'Adams', 'Williams'), 91938208, 'RoAdams@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024034671 ': [('Daniel', 'Adams', 'Keller'), 89022059, 'DaAdams@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024039733 ': [('Anthony', 'Cannon', 'Quinn'), 68414242, 'AnCannon@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024033230 ': [('Sharon', 'Brown', 'Kelley'), 73925009, 'ShBrown@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024038593 ': [('Rhonda', 'Franklin', 'Cohen'), 98133967, 'RhFranklin@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024039801 ': [('Zachary', 'Ochoa', 'Woods'), 85012227, 'ZaOchoa@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024036860 ': [('Kevin', 'Wiley', 'Henry'), 93155794, 'KeWiley@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024034086 ': [('Lisa', 'Hunter', 'Moon'), 69673913, 'LiHunter@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024036642 ': [('Jeremy', 'Stewart', 'Fischer'), 81169087, 'JeStewart@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024034913 ': [('Suzanne', 'Hayes', 'Lambert'), 66720610, 'SuHayes@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024032440 ': [('Jessica', 'Vasquez', 'Romero'), 67526161, 'JeVasquez@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024037928 ': [('Maria', 'Baker', 'Stephens'), 63802124, 'MarBaker2@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024039845 ': [('Sharon', 'Reid', 'Diaz'), 76541848, 'ShReid@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024038735 ': [('Adam', 'Hunt', 'Dean'), 93962212, 'AdHunt@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024034885 ': [('Ashley', 'Dennis', 'Brown'), 88431770, 'AsDennis@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024036738 ': [('Mary', 'Thompson', 'Wilkins'), 99129632, 'MaThompson@estudiantec.cr', 'CTLSJ', 'Bachillerato en Administración de Empresas', 0] ,
' 2024038812 ': [('Nicole', 'Dunn', 'Dickson'), 71450746, 'NiDunn@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024037359 ': [('Maureen', 'Watson', 'Williams'), 64988235, 'MaWatson@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024035286 ': [('Justin', 'Bean', 'Keller'), 93640374, 'JuBean@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024039772 ': [('Kristina', 'Calhoun', 'Stephens'), 98720328, 'KrCalhoun@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024033204 ': [('Melissa', 'Hurley', 'Cook'), 93190615, 'MeHurley@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024038820 ': [('Nicole', 'Brown', 'Sanders'), 78390514, 'NiBrown@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024037847 ': [('Caitlyn', 'Jennings', 'Barker'), 60683041, 'CaJennings@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024036876 ': [('Karen', 'Flowers', 'Flores'), 73783193, 'KaFlowers@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024035880 ': [('Brenda', 'Jackson', 'Flores'), 81430951, 'BrJackson@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024031873 ': [('Wanda', 'Church', 'Smith'), 95413976, 'WaChurch@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024036919 ': [('Rebecca', 'Cook', 'Pollard'), 64900378, 'ReCook@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024034776 ': [('David', 'Lynch', 'Morales'), 75654727, 'DaLynch@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024032183 ': [('Timothy', 'Gill', 'Powers'), 73669691, 'TiGill@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024032656 ': [('Jonathan', 'Stewart', 'Johnson'), 84524003, 'JoStewart@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024032929 ': [('Tricia', 'Ingram', 'Lee'), 61153157, 'TrIngram@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024037776 ': [('Dustin', 'Wilson', 'Austin'), 91574778, 'DuWilson@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024031847 ': [('Brittany', 'Robertson', 'Patel'), 66084201, 'BrRobertson@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024038209 ': [('Andrew', 'Hardin', 'Stone'), 65669752, 'AnHardin@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024037570 ': [('Michelle', 'Barnes', 'Smith'), 60209154, 'MiBarnes@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024034302 ': [('Christopher', 'Ray', 'Brown'), 85456530, 'ChRay@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024036235 ': [('Caleb', 'Hicks', 'Griffith'), 70789135, 'CaHicks@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024033664 ': [('Taylor', 'Nguyen', 'Castillo'), 92664510, 'TaNguyen@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024033021 ': [('Jose', 'Lawson', 'Alvarado'), 82930574, 'JoLawson@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024033844 ': [('David', 'Jones', 'Ferguson'), 98191396, 'DavJones7@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024033050 ': [('Philip', 'Hernandez', 'Stone'), 64306111, 'PhHernandez@estudiantec.cr', 'CTLSJ', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024039976 ': [('Robert', 'Anderson', 'Adams'), 95877839, 'RoAnderson@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024037602 ': [('Rebecca', 'Weaver', 'Ramirez'), 78416959, 'ReWeaver@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024034077 ': [('Sarah', 'Alvarez', 'Bowman'), 61188111, 'SaAlvarez@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024033515 ': [('Amy', 'Sandoval', 'Bridges'), 78894432, 'AmSandoval@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024032474 ': [('Shelby', 'Young', 'Williams'), 77378458, 'ShYoung@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024036195 ': [('Michael', 'York', 'Wilson'), 90172559, 'MiYork@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024035573 ': [('Cindy', 'Galloway', 'Ellis'), 87889761, 'CiGalloway@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024039315 ': [('Amber', 'Holmes', 'Smith'), 63421528, 'AmHolmes@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024036940 ': [('Brittany', 'Williams', 'Parker'), 81194997, 'BrWilliams@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024036790 ': [('Brenda', 'Gomez', 'Middleton'), 91155681, 'BrGomez@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024032928 ': [('Audrey', 'Johnson', 'Petty'), 76710659, 'AuJohnson@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024035596 ': [('Samantha', 'Savage', 'Moreno'), 63566694, 'SaSavage@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024037806 ': [('Patricia', 'Hicks', 'Davenport'), 86449010, 'PaHicks@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024031534 ': [('Marcus', 'Neal', 'Holloway'), 83222077, 'MaNeal@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024031991 ': [('Ricky', 'Jimenez', 'Hernandez'), 76223911, 'RiJimenez@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024036284 ': [('Nathan', 'Miller', 'Beard'), 95460657, 'NaMiller@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024037890 ': [('Donna', 'Alvarado', 'Anderson'), 78471879, 'DoAlvarado@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024039574 ': [('Lawrence', 'Adams', 'Meyer'), 80632550, 'LaAdams@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024034680 ': [('Katherine', 'Gallagher', 'Meyer'), 82477472, 'KaGallagher@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024039840 ': [('Andrew', 'Vega', 'Salazar'), 76990415, 'AnVega@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024033281 ': [('Austin', 'Miles', 'Perez'), 97938818, 'AuMiles@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024035497 ': [('Alexander', 'Burton', 'Acosta'), 65324720, 'AlBurton@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024036834 ': [('Hannah', 'Collins', 'Dougherty'), 74400747, 'HaCollins@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024034578 ': [('Jacob', 'Robinson', 'Casey'), 79168938, 'JaRobinson@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024038718 ': [('Maria', 'Faulkner', 'Watson'), 61623689, 'MaFaulkner@estudiantec.cr', 'CTLSJ', 'Licenciatura en Arquitectura', 0] ,
' 2024056004 ': [('Deborah', 'Murphy', 'Robinson'), 87777404, 'DeMurphy@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024052935 ': [('Julia', 'Wu', 'Gibson'), 68372554, 'JuWu@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024059135 ': [('Danielle', 'Santiago', 'Gallagher'), 78538600, 'DaSantiago@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024054729 ': [('Thomas', 'Miller', 'White'), 84943835, 'ThMiller@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024058444 ': [('Denise', 'Wilson', 'Campos'), 89007720, 'DeWilson@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024055041 ': [('Brandon', 'Huerta', 'Sanford'), 86837474, 'BrHuerta@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024058545 ': [('Adrian', 'Kelly', 'Dean'), 79588984, 'AdKelly@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024059538 ': [('Donald', 'Miles', 'Cooper'), 96242525, 'DoMiles@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024058196 ': [('Jessica', 'Walters', 'Stevens'), 68099587, 'JeWalters@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024056378 ': [('Ryan', 'Cooper', 'Neal'), 75091329, 'RyCooper@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024052975 ': [('Amy', 'Buck', 'Macias'), 79517342, 'AmBuck@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024054046 ': [('Scott', 'Malone', 'Warner'), 77751287, 'ScMalone@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024059141 ': [('Johnathan', 'Russell', 'Gutierrez'), 89120896, 'JoRussell@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024059656 ': [('Amy', 'Dominguez', 'Moore'), 77771644, 'AmDominguez@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024055414 ': [('Julie', 'Johnson', 'Davis'), 90954769, 'JuJohnson@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024054388 ': [('Amanda', 'Aguilar', 'Walker'), 76494696, 'AmAguilar@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024054690 ': [('Preston', 'Gordon', 'Ford'), 66204846, 'PrGordon@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024056127 ': [('Christina', 'Fuentes', 'Johnson'), 83552913, 'ChFuentes@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024054564 ': [('Matthew', 'Fry', 'Wood'), 74041905, 'MaFry@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024059555 ': [('Ryan', 'Williamson', 'Chavez'), 85336352, 'RyWilliamson@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024059597 ': [('Eric', 'Anderson', 'Coleman'), 94413595, 'ErAnderson@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024059414 ': [('Brittney', 'Gordon', 'Williams'), 97277114, 'BrGordon@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024059559 ': [('Renee', 'Clark', 'Khan'), 60540116, 'ReClark@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024052257 ': [('Douglas', 'Hernandez', 'Simpson'), 77055472, 'DoHernandez@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024057907 ': [('Tina', 'Brown', 'Reyes'), 74904109, 'TiBrown@estudiantec.cr', 'CAL', 'Bachillerato en Administración de Empresas', 0] ,
' 2024052439 ': [('Kayla', 'Chan', 'Pierce'), 79566407, 'KaChan@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024053588 ': [('Anthony', 'Rollins', 'Lucas'), 99139919, 'AnRollins@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024059540 ': [('Luis', 'Johnson', 'Miller'), 80737129, 'LuJohnson@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024053166 ': [('Jessica', 'Cox', 'Kelley'), 62878357, 'JeCox@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024052061 ': [('Nicholas', 'Duke', 'Davis'), 79300082, 'NiDuke@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024056558 ': [('Christopher', 'Graves', 'Parker'), 97001969, 'ChGraves@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024057161 ': [('Christina', 'Johnston', 'Wallace'), 91839760, 'ChJohnston@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024059892 ': [('Rodney', 'Ayala', 'Williams'), 90694930, 'RoAyala@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024059491 ': [('Michael', 'Chavez', 'Butler'), 89923098, 'MiChavez@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024059663 ': [('Paul', 'Stephenson', 'Burke'), 95790307, 'PaStephenson@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024055686 ': [('Kathryn', 'Rice', 'Bates'), 71806425, 'KaRice@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024059997 ': [('Joshua', 'Sanchez', 'Wilkerson'), 82760110, 'JoSanchez@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024051951 ': [('Christopher', 'Daniel', 'Green'), 61460134, 'ChDaniel@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024056741 ': [('Melissa', 'Freeman', 'Richardson'), 88901064, 'MeFreeman@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024051270 ': [('Megan', 'Scott', 'Hudson'), 75677772, 'MeScott@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024056302 ': [('Amanda', 'Rivera', 'Berg'), 65787702, 'AmRivera@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024051075 ': [('Juan', 'Parks', 'Willis'), 62557987, 'JuParks@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024055150 ': [('David', 'Cook', 'Fuentes'), 60534373, 'DaCook@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024055957 ': [('Lori', 'Bright', 'Key'), 81552520, 'LoBright@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024055550 ': [('Rachel', 'Schneider', 'Hunter'), 94080886, 'RaSchneider@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024052619 ': [('Kim', 'Kerr', 'Lam'), 67093757, 'KiKerr@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024055165 ': [('Erica', 'Green', 'Hodges'), 92318184, 'ErGreen@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024056166 ': [('Daniel', 'Conner', 'Murphy'), 77433108, 'DaConner@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024055325 ': [('Curtis', 'Doyle', 'Brown'), 73734322, 'CuDoyle@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024058938 ': [('Michael', 'Holmes', 'Brown'), 68200342, 'MiHolmes@estudiantec.cr', 'CAL', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024056880 ': [('Paul', 'Martin', 'Bell'), 98397317, 'PaMartin@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024053239 ': [('Sharon', 'Ramos', 'Boyer'), 92412005, 'ShRamos@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024051126 ': [('Melissa', 'Petersen', 'Kim'), 77128699, 'MePetersen@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024059227 ': [('Scott', 'Smith', 'Edwards'), 95979803, 'ScSmith@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024053335 ': [('Christopher', 'Farmer', 'Norris'), 67843548, 'ChFarmer@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024052178 ': [('Eric', 'Mueller', 'Rogers'), 68659115, 'ErMueller@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024056607 ': [('Steven', 'Lawrence', 'Hamilton'), 89104004, 'StLawrence@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024052054 ': [('Valerie', 'Kramer', 'Smith'), 84702549, 'VaKramer@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024056609 ': [('Michael', 'Morton', 'Maldonado'), 86294091, 'MiMorton@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024055310 ': [('Laura', 'Mccoy', 'Zimmerman'), 96209453, 'LaMccoy@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024053630 ': [('Johnny', 'Robbins', 'Nelson'), 99953687, 'JoRobbins@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024059697 ': [('Candice', 'Lamb', 'Valenzuela'), 98068493, 'CaLamb@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024055372 ': [('Samuel', 'Walsh', 'West'), 96118904, 'SaWalsh@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024051689 ': [('Olivia', 'Zimmerman', 'Ball'), 70126842, 'OlZimmerman@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024056468 ': [('Tyler', 'Oneal', 'Garcia'), 89795788, 'TyOneal@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024058870 ': [('Vanessa', 'Miller', 'Stephenson'), 62159771, 'VaMiller@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024059887 ': [('Samuel', 'Rojas', 'Trujillo'), 72528694, 'SaRojas@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024057275 ': [('Gregory', 'Kelley', 'Wilkerson'), 86513254, 'GrKelley@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024053001 ': [('Robin', 'Bailey', 'Hardin'), 60032952, 'RoBailey@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024054029 ': [('Scott', 'Roberts', 'Rodriguez'), 61346605, 'ScRoberts@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024057403 ': [('Brandi', 'Smith', 'White'), 64941116, 'BrSmith@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024057360 ': [('Bridget', 'Ramos', 'King'), 95810451, 'BrRamos@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024059476 ': [('Mary', 'Edwards', 'Myers'), 90432361, 'MaEdwards@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024052819 ': [('Vicki', 'Morrow', 'Hughes'), 61846572, 'ViMorrow@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024052858 ': [('Jessica', 'Salas', 'Riggs'), 94682556, 'JeSalas@estudiantec.cr', 'CAL', 'Bachillerato en Producción Industrial,  Limón', 0] ,
' 2024016936 ': [('Brandon', 'Blackwell', 'Rice'), 81605805, 'BrBlackwell@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024013522 ': [('Jacqueline', 'Castillo', 'Barrett'), 95343260, 'JaCastillo@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024015657 ': [('Cynthia', 'Armstrong', 'Moore'), 74620540, 'CyArmstrong@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024019760 ': [('Damon', 'Stein', 'King'), 67681454, 'DaStein@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024012513 ': [('Tyler', 'Wright', 'Carrillo'), 94637006, 'TyWright@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024014184 ': [('Todd', 'Hensley', 'Madden'), 65606604, 'ToHensley@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024012569 ': [('Jeremy', 'Murray', 'Le'), 99057161, 'JeMurray@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024014535 ': [('Deborah', 'Chambers', 'Thompson'), 93505467, 'DeChambers@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024013319 ': [('Steven', 'Murphy', 'Sullivan'), 83790598, 'StMurphy@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024018892 ': [('Christine', 'Bowman', 'Grimes'), 72741997, 'ChBowman@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024019302 ': [('Carrie', 'Moreno', 'Bernard'), 89187337, 'CaMoreno@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024012109 ': [('Matthew', 'Soto', 'Gilbert'), 88754741, 'MaSoto@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024014057 ': [('Erin', 'Delgado', 'Miller'), 76172233, 'ErDelgado@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024014026 ': [('Vanessa', 'Rodriguez', 'Barber'), 67367841, 'VaRodriguez@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024018644 ': [('Dawn', 'Jensen', 'Morales'), 62422216, 'DaJensen@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024019075 ': [('Matthew', 'Robinson', 'Smith'), 89130645, 'MaRobinson@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024016423 ': [('Kelsey', 'Wheeler', 'Lambert'), 89826649, 'KeWheeler@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024015633 ': [('Christian', 'Russo', 'Davis'), 61632534, 'ChRusso@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024019332 ': [('Alejandro', 'Zavala', 'Brown'), 96312864, 'AlZavala@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024016567 ': [('Pamela', 'Fischer', 'Levy'), 76170518, 'PaFischer@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024014636 ': [('Brian', 'Brewer', 'Foster'), 65050395, 'BrBrewer@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024015376 ': [('Tina', 'Porter', 'Holmes'), 87183151, 'TiPorter@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024017278 ': [('Mike', 'Harrison', 'Robbins'), 61182543, 'MiHarrison@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024015076 ': [('Robert', 'Stein', 'Miranda'), 89022524, 'RoStein@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024019696 ': [('Michele', 'Brown', 'Taylor'), 70971775, 'MiBrown@estudiantec.cr', 'CTCC', 'Bachillerato en Administración de Empresas', 0] ,
' 2024018963 ': [('Kayla', 'Glover', 'Martinez'), 76253000, 'KaGlover@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024015594 ': [('Jerry', 'Young', 'Farmer'), 65350218, 'JeYoung@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024016454 ': [('Amber', 'Barrera', 'Roberts'), 97410365, 'AmBarrera@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024018399 ': [('Thomas', 'Owens', 'Peters'), 94853548, 'ThOwens@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024013512 ': [('Theresa', 'Holmes', 'Mitchell'), 77706061, 'ThHolmes@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024014044 ': [('Michelle', 'Ramirez', 'Ramirez'), 75342007, 'MiRamirez@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024012361 ': [('Willie', 'Goodwin', 'Flynn'), 91208418, 'WiGoodwin@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024015255 ': [('Jeffrey', 'Johnson', 'Miller'), 88388110, 'JefJohnson4@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024015829 ': [('Zachary', 'Osborne', 'Brown'), 80654611, 'ZaOsborne@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024014958 ': [('Michael', 'Anderson', 'Barnes'), 71691346, 'MiAnderson@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024018155 ': [('Rachel', 'Hendrix', 'Crane'), 60694495, 'RaHendrix@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024018299 ': [('Ashley', 'Martinez', 'Carter'), 63217819, 'AsMartinez@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024011276 ': [('Juan', 'Clark', 'Humphrey'), 65986516, 'JuClark@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024013324 ': [('James', 'Burke', 'Ramirez'), 84800915, 'JaBurke@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024011844 ': [('Sean', 'Garrett', 'Alvarez'), 64254268, 'SeGarrett@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024015950 ': [('Caleb', 'Howell', 'Whitehead'), 93691309, 'CaHowell@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024011471 ': [('Robert', 'Farley', 'Warren'), 95404279, 'RoFarley@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024015952 ': [('Tiffany', 'Bell', 'Wilson'), 86767174, 'TiBell@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024016171 ': [('Joseph', 'King', 'House'), 91346160, 'JoKing@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024014602 ': [('Aaron', 'Vance', 'Cunningham'), 63241981, 'AaVance@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024011794 ': [('Angela', 'Hunt', 'Nelson'), 71334245, 'AnHunt@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024013806 ': [('Gloria', 'Nichols', 'Mason'), 66492335, 'GlNichols@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024013041 ': [('Kyle', 'Aguilar', 'Allen'), 60008463, 'KyAguilar@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024015955 ': [('Savannah', 'Petersen', 'Williams'), 88003725, 'SaPetersen@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024013163 ': [('William', 'Daniels', 'Shaw'), 82279645, 'WiDaniels@estudiantec.cr', 'CTCC', 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0] ,
' 2024016811 ': [('Lawrence', 'Nguyen', 'Lee'), 70067500, 'LaNguyen@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024014138 ': [('Kelli', 'Torres', 'Potter'), 96148485, 'KeTorres@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024011531 ': [('Tanya', 'Ward', 'Delgado'), 66498231, 'TaWard@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024011694 ': [('Kevin', 'Baker', 'Sims'), 82560344, 'KeBaker@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024011070 ': [('Jennifer', 'Casey', 'Lopez'), 89117085, 'JeCasey@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024016123 ': [('Elizabeth', 'Evans', 'Murphy'), 70460308, 'ElEvans@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024014331 ': [('Timothy', 'Tyler', 'Villa'), 72428234, 'TiTyler@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024012413 ': [('Jeffrey', 'Smith', 'Hernandez'), 62501639, 'JeSmith@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024012055 ': [('Jerry', 'Romero', 'Abbott'), 63241949, 'JeRomero@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024017280 ': [('John', 'Wallace', 'Clark'), 94422627, 'JoWallace@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024018323 ': [('Alicia', 'Park', 'Jacobs'), 75409321, 'AlPark@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024016370 ': [('Gerald', 'Young', 'Dunn'), 90301417, 'GeYoung@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024017899 ': [('Tyler', 'Sawyer', 'Davis'), 71894000, 'TySawyer@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024013988 ': [('Brittney', 'Parker', 'Salazar'), 93384393, 'BrParker@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024017123 ': [('Michael', 'Franklin', 'King'), 86625308, 'MiFranklin@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024014689 ': [('Linda', 'Hensley', 'Leonard'), 64415314, 'LiHensley@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024014773 ': [('Kerri', 'Taylor', 'Massey'), 88084121, 'KeTaylor@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024013171 ': [('Timothy', 'Holland', 'Graham'), 83075108, 'TiHolland@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024018203 ': [('Michael', 'Ford', 'Reed'), 93477379, 'MiFord@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024014526 ': [('William', 'Barajas', 'Coleman'), 73487356, 'WiBarajas@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024019326 ': [('Kelly', 'Stewart', 'Gardner'), 98714253, 'KeStewart@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024011480 ': [('Nicole', 'Cruz', 'Barron'), 85814166, 'NiCruz@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024016186 ': [('Jamie', 'Wallace', 'Scott'), 98197106, 'JaWallace@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024018100 ': [('Donna', 'Jenkins', 'Hooper'), 65335207, 'DoJenkins@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024017374 ': [('John', 'Richards', 'Anderson'), 94598032, 'JoRichards@estudiantec.cr', 'CTCC', 'Bachillerato en Gestión del Turismo Sostenible', 0] ,
' 2024019626 ': [('Jasmine', 'Dunn', 'Pacheco'), 82906214, 'JaDunn@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024016200 ': [('Pamela', 'Cruz', 'Hernandez'), 61457592, 'PaCruz@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024017080 ': [('Valerie', 'Martinez', 'Clark'), 79051882, 'VaMartinez@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024012668 ': [('Deborah', 'Johnson', 'Harper'), 85215697, 'DeJohnson@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024018781 ': [('David', 'Hernandez', 'Brady'), 82709668, 'DaHernandez@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024013223 ': [('Sandy', 'Mitchell', 'Pearson'), 64552031, 'SaMitchell@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024016517 ': [('Timothy', 'Yates', 'Stephenson'), 68028183, 'TiYates@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024013005 ': [('Kristopher', 'Roy', 'Carey'), 86145302, 'KrRoy@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024012057 ': [('Amanda', 'Thompson', 'Cooper'), 96244650, 'AmThompson@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024013906 ': [('Drew', 'Daniels', 'Miller'), 81560676, 'DrDaniels@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024018193 ': [('Marie', 'Cortez', 'Shields'), 78763948, 'MaCortez@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024011683 ': [('Martha', 'Taylor', 'Gardner'), 85288683, 'MaTaylor@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024019020 ': [('Chris', 'Price', 'Higgins'), 93842632, 'ChrPrice5@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024016481 ': [('Anthony', 'Woodard', 'Carlson'), 66633438, 'AnWoodard@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024015299 ': [('Michael', 'Bush', 'Long'), 62519052, 'MiBush@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024012155 ': [('Robin', 'Jones', 'Kelly'), 80089092, 'RoJones@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024011651 ': [('James', 'Griffin', 'Schroeder'), 91199827, 'JaGriffin@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024014023 ': [('David', 'Fisher', 'Smith'), 97056789, 'DaFisher@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024011778 ': [('Matthew', 'Sharp', 'Richardson'), 70688674, 'MaSharp@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024019266 ': [('Carmen', 'Carlson', 'Hanson'), 67446581, 'CaCarlson@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024018046 ': [('Samuel', 'Hudson', 'Reid'), 64854576, 'SaHudson@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024015977 ': [('Edward', 'Brown', 'Miller'), 63322146, 'EdBrown@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024015595 ': [('David', 'Chavez', 'Lawrence'), 71318506, 'DaChavez@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024014191 ': [('Anthony', 'Graves', 'Snyder'), 74507453, 'AnGraves@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024018468 ': [('Phyllis', 'Glass', 'Johnson'), 88180848, 'PhGlass@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Biotecnología', 0] ,
' 2024011182 ': [('Samantha', 'Anderson', 'Miranda'), 78594830, 'SaAnderson@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024014064 ': [('Adam', 'Nunez', 'Kennedy'), 82801129, 'AdNunez@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024014990 ': [('Virginia', 'Oconnor', 'Mitchell'), 80250834, 'ViOconnor@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024011796 ': [('Gabriella', 'Ramirez', 'Collins'), 97475354, 'GaRamirez@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024018127 ': [('Janet', 'Williams', 'Parker'), 76217712, 'JaWilliams@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024019496 ': [('Cynthia', 'Pratt', 'Wheeler'), 63087569, 'CyPratt@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024016952 ': [('James', 'Smith', 'Thompson'), 61758735, 'JaSmith@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024016290 ': [('Laura', 'Williams', 'Beasley'), 82838000, 'LaWilliams@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024019401 ': [('Chad', 'Howard', 'Avila'), 84221164, 'ChHoward@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024012271 ': [('Ryan', 'Bailey', 'Kim'), 67310816, 'RyBailey@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024015411 ': [('Michael', 'Garcia', 'Jones'), 92818254, 'MiGarcia@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024015462 ': [('Charles', 'Hughes', 'Harrington'), 70526917, 'ChHughes@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024014670 ': [('James', 'Smith', 'Lozano'), 88216533, 'JamSmith7@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024011680 ': [('Stephanie', 'Adkins', 'Matthews'), 66711494, 'StAdkins@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024014538 ': [('Cynthia', 'James', 'Greene'), 67651441, 'CyJames@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024019593 ': [('Amy', 'Brewer', 'Rodriguez'), 84527340, 'AmBrewer@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024014326 ': [('Walter', 'Griffith', 'Andrews'), 96340973, 'WaGriffith@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024016244 ': [('Emily', 'Shepherd', 'Fuentes'), 72407942, 'EmShepherd@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024013742 ': [('Susan', 'Rangel', 'Blevins'), 98355718, 'SuRangel@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024017011 ': [('Jonathan', 'Phillips', 'Mccoy'), 86222891, 'JoPhillips@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024015451 ': [('Erin', 'Schroeder', 'Lewis'), 61966595, 'ErSchroeder@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024017149 ': [('Thomas', 'Luna', 'Mckee'), 60362854, 'ThLuna@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024017189 ': [('Kathleen', 'Smith', 'Griffin'), 64542461, 'KaSmith@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024015757 ': [('Mark', 'Floyd', 'Bell'), 90899939, 'MaFloyd@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024019987 ': [('Julie', 'Long', 'Flores'), 72841624, 'JuLong@estudiantec.cr', 'CTCC', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024015869 ': [('James', 'Cruz', 'Mathis'), 66784594, 'JaCruz@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024013486 ': [('Veronica', 'Rice', 'Cooper'), 80710146, 'VeRice@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024018933 ': [('Melissa', 'Kidd', 'Clark'), 84712298, 'MeKidd@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024014080 ': [('Isabel', 'Hoffman', 'Jenkins'), 77526243, 'IsHoffman@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024012623 ': [('Alexander', 'Chan', 'Mcguire'), 99485575, 'AlChan@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024012396 ': [('Michael', 'Williams', 'Ellison'), 72345834, 'MiWilliams@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024014102 ': [('Gabriel', 'Walker', 'Jennings'), 97931320, 'GaWalker@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024011035 ': [('Chad', 'Wolfe', 'Smith'), 93972572, 'ChWolfe@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024016671 ': [('Maria', 'Bautista', 'Madden'), 87209374, 'MarBautista4@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024013110 ': [('Gregory', 'Parker', 'Wheeler'), 69617106, 'GrParker@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024014551 ': [('Stephanie', 'Brown', 'Perkins'), 80039012, 'StBrown@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024019684 ': [('Gary', 'Sanchez', 'Freeman'), 87447673, 'GaSanchez@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024017578 ': [('Christine', 'Medina', 'Rosario'), 97720007, 'ChMedina@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024011526 ': [('Stephen', 'Martinez', 'Eaton'), 91870524, 'StMartinez@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024017002 ': [('Patricia', 'Roberts', 'Rush'), 95017461, 'PaRoberts@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024018365 ': [('Susan', 'Clark', 'Duarte'), 65407569, 'SuClark@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024019281 ': [('Samantha', 'Flores', 'Olson'), 71353572, 'SaFlores@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024018259 ': [('Jeffrey', 'Briggs', 'Lewis'), 75158208, 'JeBriggs@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024019249 ': [('Virginia', 'Pacheco', 'Lang'), 99669285, 'ViPacheco@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024012516 ': [('Michelle', 'Sharp', 'Solis'), 88055550, 'MiSharp@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024019966 ': [('Robert', 'Moody', 'Martinez'), 95513512, 'RoMoody@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024019409 ': [('Sarah', 'Thomas', 'Mclaughlin'), 70019244, 'SaThomas@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024015879 ': [('Margaret', 'Williams', 'Hawkins'), 97089365, 'MaWilliams@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024017706 ': [('Andrew', 'Fowler', 'Turner'), 94614566, 'AnFowler@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024011791 ': [('Steve', 'Conner', 'Brewer'), 88561762, 'StConner@estudiantec.cr', 'CTCC', 'Licenciatura en Administración de Tecnología de Información', 0] ,
' 2024019728 ': [('Sara', 'Barnes', 'Lowe'), 72724323, 'SaBarnes@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024017756 ': [('William', 'Brown', 'Barry'), 79039971, 'WiBrown@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024015450 ': [('Kimberly', 'Burch', 'Jackson'), 72216951, 'KiBurch@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024016366 ': [('Kathleen', 'Burnett', 'Bryant'), 95969840, 'KaBurnett@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024017212 ': [('Claudia', 'Floyd', 'Buck'), 61085911, 'ClFloyd@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024015047 ': [('Caitlin', 'Martinez', 'Howard'), 99172118, 'CaMartinez@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024018816 ': [('Tamara', 'Cruz', 'Roy'), 76581483, 'TaCruz@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024015244 ': [('John', 'Peterson', 'Peck'), 82695983, 'JoPeterson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024012437 ': [('Susan', 'Townsend', 'Atkins'), 62961840, 'SuTownsend@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024012620 ': [('Timothy', 'Torres', 'Thomas'), 61729737, 'TiTorres@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024011767 ': [('Stacey', 'Rivera', 'Nelson'), 76671100, 'StRivera@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024015069 ': [('Alexandra', 'Walker', 'Klein'), 71358467, 'AlWalker@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024013738 ': [('Gregory', 'Conrad', 'Sanders'), 99693617, 'GrConrad@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024011415 ': [('Steven', 'Taylor', 'Roach'), 73294414, 'StTaylor@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024013576 ': [('Mark', 'Murphy', 'Bates'), 76001318, 'MarMurphy4@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024011761 ': [('Jerry', 'Horn', 'Turner'), 82224409, 'JeHorn@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024015584 ': [('Tyler', 'Mcpherson', 'Carney'), 92030726, 'TyMcpherson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024011040 ': [('April', 'Jones', 'Myers'), 78157057, 'ApJones@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024011597 ': [('Nathan', 'Jones', 'Edwards'), 65562100, 'NaJones@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024017537 ': [('Belinda', 'Keith', 'Blair'), 71672870, 'BeKeith@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024018512 ': [('Patrick', 'Bond', 'Moore'), 61444514, 'PaBond@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024012053 ': [('Lisa', 'Roberts', 'Hernandez'), 80563938, 'LiRoberts@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024011982 ': [('Kristin', 'Ellis', 'Berry'), 91734491, 'KrEllis@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024013803 ': [('Dillon', 'Castro', 'Price'), 60789116, 'DiCastro@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024014662 ': [('David', 'Kelly', 'Dixon'), 62705163, 'DaKelly@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Agrícola', 0] ,
' 2024017448 ': [('Mary', 'Medina', 'Nelson'), 78913790, 'MaMedina@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024011851 ': [('Paul', 'Ford', 'Newton'), 95481650, 'PaFord@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024019122 ': [('Shawn', 'Green', 'Hernandez'), 66058957, 'ShGreen@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024019595 ': [('Dawn', 'Hawkins', 'Contreras'), 80374700, 'DaHawkins@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024019649 ': [('Johnny', 'Olson', 'Douglas'), 67823181, 'JoOlson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024015790 ': [('Ashley', 'Allen', 'Trevino'), 62468782, 'AsAllen@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024012526 ': [('Ralph', 'Sellers', 'Hill'), 67652602, 'RaSellers@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024017198 ': [('Susan', 'Bailey', 'James'), 81292553, 'SuBailey@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024016957 ': [('Charlotte', 'West', 'Harmon'), 84010763, 'ChWest@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024014783 ': [('Amanda', 'Harris', 'Davis'), 78853135, 'AmHarris@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024019666 ': [('Kimberly', 'Fisher', 'Burgess'), 71261210, 'KiFisher@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024011064 ': [('Daniel', 'Simon', 'Fisher'), 79873867, 'DaSimon@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024017779 ': [('Lauren', 'Smith', 'Best'), 94232349, 'LaSmith@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024016093 ': [('Christina', 'Ingram', 'Chandler'), 65857458, 'ChIngram@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024019897 ': [('Jeffrey', 'Stone', 'Marshall'), 78498926, 'JeStone@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024015388 ': [('Monica', 'Davis', 'Taylor'), 61336529, 'MoDavis@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024012402 ': [('Ashley', 'Jones', 'Wilson'), 75732154, 'AsJones@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024014274 ': [('Donna', 'Alvarez', 'Mcgee'), 64236123, 'DoAlvarez@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024013186 ': [('Victoria', 'Campbell', 'Price'), 61642194, 'ViCampbell@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024017079 ': [('Lauren', 'Smith', 'Woodward'), 98523382, 'LauSmith9@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024012660 ': [('Melissa', 'Warner', 'Walker'), 74708144, 'MeWarner@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024017999 ': [('Donna', 'Green', 'Brown'), 65796395, 'DoGreen@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024018577 ': [('Emily', 'Yang', 'Martinez'), 74342651, 'EmYang@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024015349 ': [('Emma', 'Gill', 'Fischer'), 65585781, 'EmGill@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024012627 ': [('Anthony', 'Thomas', 'Hodges'), 77089936, 'AnThomas@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Ambiental', 0] ,
' 2024015503 ': [('Lynn', 'Gray', 'Berry'), 94910485, 'LyGray@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024019641 ': [('Timothy', 'Ewing', 'Harris'), 80535401, 'TiEwing@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024017968 ': [('Roger', 'Olson', 'Anderson'), 74236455, 'RoOlson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024014861 ': [('Brenda', 'Diaz', 'Ryan'), 81509463, 'BrDiaz@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024018349 ': [('Eddie', 'Green', 'Wolfe'), 64390260, 'EdGreen@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024016907 ': [('Jonathan', 'Ingram', 'Burton'), 88497665, 'JoIngram@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024017032 ': [('Randall', 'Hinton', 'Obrien'), 81661675, 'RaHinton@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024011598 ': [('Todd', 'Duncan', 'Meyer'), 97012626, 'ToDuncan@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024014994 ': [('Samuel', 'Johnson', 'Phillips'), 66510143, 'SaJohnson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024015658 ': [('Amber', 'Mcconnell', 'King'), 80420319, 'AmMcconnell@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024018004 ': [('Cynthia', 'Davidson', 'Howell'), 93790044, 'CyDavidson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024014871 ': [('Henry', 'Jones', 'Carroll'), 66871379, 'HeJones@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024012078 ': [('Matthew', 'Smith', 'Walls'), 74510880, 'MaSmith@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024014951 ': [('Dana', 'Jordan', 'Dominguez'), 85416705, 'DaJordan@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024012409 ': [('Amanda', 'Daugherty', 'Butler'), 81628921, 'AmDaugherty@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024016600 ': [('Kathryn', 'Stone', 'Andrews'), 67537774, 'KaStone@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024016140 ': [('Katherine', 'Humphrey', 'Green'), 90962788, 'KaHumphrey@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024018847 ': [('Sierra', 'Adkins', 'Williams'), 87850582, 'SiAdkins@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024019984 ': [('Bryan', 'Vazquez', 'Beard'), 73934832, 'BrVazquez@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024017130 ': [('Brian', 'Trevino', 'Walker'), 77763756, 'BrTrevino@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024016612 ': [('Tara', 'Garcia', 'Smith'), 76346495, 'TaGarcia@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024012381 ': [('Michael', 'Bowman', 'Young'), 83494206, 'MiBowman@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024014547 ': [('Jonathan', 'Oneal', 'Anderson'), 69435031, 'JoOneal@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024013602 ': [('Christopher', 'Casey', 'Singh'), 85063512, 'ChCasey@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024019394 ': [('Andrew', 'Boyd', 'Blevins'), 81523163, 'AnBoyd@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024018102 ': [('Benjamin', 'Oliver', 'Simmons'), 74616380, 'BeOliver@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024019540 ': [('Jacob', 'Perez', 'Taylor'), 71545917, 'JaPerez@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024015097 ': [('Arthur', 'Lang', 'Bullock'), 62232387, 'ArLang@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024015929 ': [('Evelyn', 'Ramos', 'Gray'), 88564483, 'EvRamos@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024012245 ': [('John', 'Garza', 'Peterson'), 68286464, 'JoGarza@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024012921 ': [('Matthew', 'Poole', 'Krause'), 93275072, 'MaPoole@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024018764 ': [('Jasmine', 'Anderson', 'Cooper'), 74895443, 'JaAnderson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024013962 ': [('Albert', 'Hernandez', 'Chandler'), 87594219, 'AlHernandez@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024015471 ': [('Antonio', 'Trevino', 'Young'), 81771323, 'AnTrevino@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024017546 ': [('Robert', 'Hayes', 'Charles'), 83412616, 'RoHayes@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024012070 ': [('Jennifer', 'Garcia', 'Jones'), 99484514, 'JeGarcia@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024014914 ': [('Deanna', 'Vang', 'Gill'), 62320452, 'DeVang@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024019250 ': [('Scott', 'Garcia', 'Estrada'), 63519429, 'ScGarcia@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024016872 ': [('Zachary', 'Barrera', 'White'), 93203073, 'ZaBarrera@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024011855 ': [('Dana', 'Martin', 'Bradley'), 70509230, 'DaMartin@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024017970 ': [('Marcia', 'Moore', 'Scott'), 95838670, 'MaMoore@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024012633 ': [('Thomas', 'Miles', 'Johnson'), 68460133, 'ThMiles@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024017247 ': [('Albert', 'Martinez', 'Williams'), 75191101, 'AlMartinez@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024011836 ': [('Suzanne', 'Ellis', 'Rocha'), 91403966, 'SuEllis@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024015438 ': [('Kyle', 'Allison', 'Berger'), 81433008, 'KyAllison@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024016109 ': [('Rhonda', 'Campos', 'Petty'), 70260777, 'RhCampos@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024012522 ': [('Kendra', 'Thompson', 'Martin'), 70304300, 'KeThompson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024017631 ': [('Angel', 'Lindsey', 'Garcia'), 65884655, 'AnLindsey@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024017867 ': [('Kristi', 'Thomas', 'Stanley'), 64263783, 'KrThomas@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024015045 ': [('Leah', 'Chambers', 'Wright'), 67217162, 'LeChambers@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Agronegocios', 0] ,
' 2024017806 ': [('Colin', 'Phillips', 'Peters'), 71592971, 'CoPhillips@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024015797 ': [('Andrea', 'Harper', 'Bates'), 61304271, 'AnHarper@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024012752 ': [('Paul', 'Thomas', 'Carr'), 87426610, 'PaThomas@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024017300 ': [('Kristina', 'Roach', 'Hubbard'), 74419020, 'KrRoach@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024018662 ': [('Maria', 'Smith', 'Owens'), 88964593, 'MarSmith8@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024015084 ': [('Jenna', 'Reed', 'Johnson'), 67993144, 'JeReed@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024014534 ': [('Dawn', 'Shah', 'Mcgrath'), 71117833, 'DaShah@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024014619 ': [('Carrie', 'King', 'Peck'), 65821849, 'CaKing@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024016724 ': [('Christopher', 'Lopez', 'Alvarez'), 68785872, 'ChLopez@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024016139 ': [('Sean', 'Reyes', 'Morton'), 89377052, 'SeReyes@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024013489 ': [('Grant', 'Dixon', 'Fischer'), 71327887, 'GrDixon@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024012502 ': [('Steven', 'Brennan', 'Morrow'), 81559415, 'StBrennan@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024014145 ': [('Jane', 'Brown', 'Ruiz'), 71321070, 'JanBrown6@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024017823 ': [('Katelyn', 'Ruiz', 'Rowland'), 76578632, 'KaRuiz@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024012322 ': [('Karen', 'Miller', 'Manning'), 95812009, 'KaMiller@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024012878 ': [('William', 'Black', 'Lambert'), 91724290, 'WiBlack@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024018135 ': [('William', 'Rice', 'Sharp'), 87380871, 'WiRice@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024019111 ': [('Daniel', 'Jackson', 'Ferrell'), 72768627, 'DaJackson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024011248 ': [('Tina', 'Davis', 'Walker'), 87685787, 'TiDavis@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024016699 ': [('Sean', 'Sutton', 'Santana'), 98809502, 'SeSutton@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024018653 ': [('Dalton', 'Hunter', 'Rubio'), 94737146, 'DaHunter@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024014061 ': [('Molly', 'Guzman', 'Hebert'), 94038211, 'MoGuzman@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024014269 ': [('Gina', 'Martin', 'Frazier'), 93242965, 'GiMartin@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024011454 ': [('John', 'Kent', 'Knight'), 79483633, 'JoKent@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024017604 ': [('Jill', 'Waters', 'Patel'), 95225759, 'JiWaters@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Computadores', 0] ,
' 2024019616 ': [('Kristine', 'Williamson', 'Young'), 81348545, 'KrWilliamson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024019568 ': [('Jacob', 'Horton', 'Stevens'), 67102650, 'JaHorton@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024016471 ': [('Alexander', 'Burch', 'Vance'), 76010510, 'AlBurch@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024015900 ': [('Joshua', 'Rivera', 'Jackson'), 76006697, 'JoRivera@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024012560 ': [('Kenneth', 'Hernandez', 'Boyd'), 75693248, 'KeHernandez@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024014999 ': [('Heather', 'Stevens', 'Arroyo'), 93964984, 'HeStevens@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024013526 ': [('Megan', 'Martin', 'Walsh'), 94150665, 'MeMartin@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024012484 ': [('Andrew', 'Thompson', 'Flynn'), 97621431, 'AnThompson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024019112 ': [('Kendra', 'Berry', 'Gallagher'), 76876108, 'KeBerry@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024018220 ': [('Eric', 'Burke', 'Lee'), 78627235, 'ErBurke@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024018345 ': [('Christina', 'Mccarthy', 'Bailey'), 94366713, 'ChMccarthy@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024018922 ': [('Troy', 'Floyd', 'Hardy'), 85472978, 'TrFloyd@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024011731 ': [('Keith', 'Hampton', 'Patterson'), 80713440, 'KeHampton@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024013632 ': [('Christopher', 'Kelly', 'Lowe'), 68460485, 'ChKelly@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024016664 ': [('Emily', 'Le', 'Francis'), 80352360, 'EmLe@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024013681 ': [('Charlene', 'Coleman', 'Wolf'), 87975206, 'ChColeman@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024013704 ': [('Matthew', 'Hoffman', 'Wilcox'), 90630061, 'MatHoffman7@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024018275 ': [('Stephanie', 'Owens', 'Marshall'), 67379304, 'StOwens@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024017749 ': [('Brittany', 'Smith', 'Valenzuela'), 64676920, 'BriSmith5@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024017050 ': [('Raymond', 'Sanchez', 'Manning'), 72501806, 'RaSanchez@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024015260 ': [('Nicole', 'Lane', 'Obrien'), 96693568, 'NiLane@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024017939 ': [('Robert', 'Sanders', 'Perez'), 97363460, 'RoSanders@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024014901 ': [('Ronald', 'Jones', 'Clarke'), 79085310, 'RonJones8@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024017993 ': [('Ryan', 'Williams', 'Johnson'), 71393250, 'RyWilliams@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024016407 ': [('Jesse', 'Weiss', 'Green'), 67274702, 'JeWeiss@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Construcción', 0] ,
' 2024013403 ': [('Patrick', 'Cook', 'Munoz'), 91464826, 'PaCook@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024018332 ': [('Anthony', 'Garcia', 'West'), 71922383, 'AnGarcia@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024013144 ': [('Kirk', 'Brooks', 'Anderson'), 61910486, 'KiBrooks@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024016738 ': [('David', 'Martinez', 'Chapman'), 90428973, 'DaMartinez@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024018546 ': [('Luis', 'White', 'Snyder'), 86314389, 'LuWhite@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024014527 ': [('Kimberly', 'Snyder', 'Chapman'), 86740228, 'KiSnyder@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024012616 ': [('Glenn', 'Thornton', 'Spencer'), 74220255, 'GlThornton@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024013276 ': [('Benjamin', 'Robinson', 'Shaw'), 89643559, 'BeRobinson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024016315 ': [('Kimberly', 'Miller', 'Waters'), 64978687, 'KiMiller@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024014608 ': [('Charles', 'Adams', 'Hickman'), 67373552, 'ChAdams@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024016023 ': [('Walter', 'Kelly', 'Mullins'), 67635629, 'WaKelly@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024017856 ': [('Tracy', 'West', 'Dickerson'), 71317028, 'TrWest@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024014851 ': [('Lindsay', 'Terry', 'Riley'), 75064931, 'LiTerry@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024015420 ': [('Nicole', 'Lee', 'Mann'), 87542824, 'NiLee@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024011325 ': [('Scott', 'Baldwin', 'Stephens'), 63856141, 'ScBaldwin@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024011658 ': [('Stephen', 'Turner', 'Palmer'), 72260434, 'StTurner@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024012457 ': [('Richard', 'Spencer', 'Brown'), 89198267, 'RiSpencer@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024013618 ': [('Barbara', 'Meyer', 'Austin'), 95073373, 'BaMeyer@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024019317 ': [('Latoya', 'Mcgee', 'Garcia'), 83087077, 'LaMcgee@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024016767 ': [('Kelly', 'Davidson', 'Barber'), 97676105, 'KeDavidson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024017471 ': [('Carla', 'Rivera', 'Warren'), 87906604, 'CaRivera@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024016146 ': [('Anthony', 'Lawrence', 'Williams'), 65561919, 'AnLawrence@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024013855 ': [('Tina', 'Mcfarland', 'Horton'), 66021929, 'TiMcfarland@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024011076 ': [('Jamie', 'Williamson', 'Barrera'), 97333110, 'JaWilliamson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024011036 ': [('Walter', 'Lee', 'Haas'), 76328858, 'WaLee@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Diseño Industrial', 0] ,
' 2024011369 ': [('Shannon', 'Mason', 'Walker'), 69400820, 'ShMason@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024013650 ': [('Haley', 'Barton', 'Hendrix'), 74596289, 'HaBarton@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024015104 ': [('Randall', 'Watkins', 'Smith'), 65477656, 'RaWatkins@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024014768 ': [('Joseph', 'Johnson', 'Smith'), 63582370, 'JosJohnson9@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024018112 ': [('Kevin', 'Harvey', 'Adams'), 91066910, 'KeHarvey@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024015895 ': [('Roy', 'Conner', 'Parker'), 86751430, 'RoConner@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024016716 ': [('Elizabeth', 'Thomas', 'Farmer'), 89484334, 'ElThomas@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024015893 ': [('Marissa', 'Gutierrez', 'White'), 67459052, 'MaGutierrez@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024019851 ': [('Autumn', 'Trujillo', 'Schneider'), 78384102, 'AuTrujillo@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024011115 ': [('Timothy', 'Kane', 'Romero'), 88193856, 'TiKane@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024018027 ': [('Barbara', 'Melton', 'Rodriguez'), 71228148, 'BaMelton@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024016991 ': [('Kevin', 'Huffman', 'Andrews'), 80243055, 'KeHuffman@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024019154 ': [('Thomas', 'Hernandez', 'Patrick'), 84873621, 'ThHernandez@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024016478 ': [('Trevor', 'Day', 'King'), 81568953, 'TrDay@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024013143 ': [('Leah', 'Martin', 'Meadows'), 60077347, 'LeMartin@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024018863 ': [('Michelle', 'Pierce', 'West'), 88724529, 'MiPierce@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024014687 ': [('Angela', 'Morrison', 'Hale'), 95679290, 'AnMorrison@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024019239 ': [('Maria', 'Jackson', 'Stephens'), 74342520, 'MaJackson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024017858 ': [('Ashley', 'Blankenship', 'Potter'), 71695705, 'AsBlankenship@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024016317 ': [('Jessica', 'Jacobs', 'Schneider'), 88792750, 'JeJacobs@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024011018 ': [('Scott', 'James', 'Anderson'), 95907122, 'ScJames@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024018096 ': [('Mark', 'Williams', 'Bell'), 73508941, 'MarWilliams9@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024012195 ': [('David', 'Krueger', 'Reynolds'), 95629859, 'DaKrueger@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024011765 ': [('Amanda', 'Chang', 'Horne'), 96470111, 'AmChang@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024013462 ': [('Kevin', 'Padilla', 'Wood'), 82123467, 'KePadilla@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Materiales', 0] ,
' 2024017493 ': [('Elizabeth', 'Higgins', 'Baird'), 77803468, 'ElHiggins@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024013496 ': [('Allison', 'Day', 'Lee'), 63725810, 'AlDay@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024011756 ': [('Matthew', 'Lee', 'Fitzpatrick'), 79086583, 'MatLee2@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024013476 ': [('Brittany', 'Johnson', 'Pruitt'), 91593981, 'BrJohnson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024016420 ': [('Penny', 'Mitchell', 'Young'), 90761092, 'PeMitchell@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024018097 ': [('Jennifer', 'Jones', 'Morales'), 60180266, 'JeJones@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024016412 ': [('Christopher', 'Allen', 'Gould'), 81665985, 'ChAllen@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024016625 ': [('Phillip', 'Li', 'Mccoy'), 84043870, 'PhLi@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024018636 ': [('Brian', 'Underwood', 'Flores'), 66313118, 'BrUnderwood@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024019531 ': [('Roberto', 'Pham', 'Hendricks'), 69530649, 'RoPham@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024015101 ': [('Robert', 'Weber', 'Sanford'), 62743501, 'RoWeber@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024012952 ': [('Christopher', 'Bailey', 'James'), 66220510, 'ChBailey@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024013092 ': [('Jose', 'Shepard', 'Carrillo'), 76275557, 'JoShepard@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024016687 ': [('Nicholas', 'Rios', 'Sherman'), 88236977, 'NiRios@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024013340 ': [('Jacqueline', 'Schultz', 'Henry'), 82544401, 'JaSchultz@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024019804 ': [('Shari', 'Torres', 'Hill'), 84204040, 'ShTorres@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024017248 ': [('Heidi', 'Conrad', 'Martinez'), 81250881, 'HeConrad@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024013533 ': [('Sarah', 'White', 'Willis'), 62485019, 'SaWhite@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024012795 ': [('Anthony', 'Cook', 'Owens'), 88390818, 'AnCook@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024019046 ': [('Christopher', 'Williams', 'Parker'), 67480824, 'ChrWilliams1@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024018087 ': [('Katherine', 'Houston', 'Santos'), 67815868, 'KaHouston@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024011014 ': [('Antonio', 'Williams', 'Phillips'), 61279975, 'AnWilliams@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024011252 ': [('Ryan', 'Scott', 'Mcmillan'), 62167560, 'RyScott@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024017831 ': [('Jonathon', 'Wilson', 'Ochoa'), 89138172, 'JoWilson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024013195 ': [('John', 'Brown', 'Payne'), 72239712, 'JoBrown@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Producción Industrial', 0] ,
' 2024011477 ': [('Anthony', 'Neal', 'West'), 82466609, 'AnNeal@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024012819 ': [('Michael', 'Jordan', 'Gordon'), 90478034, 'MiJordan@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024011091 ': [('Joel', 'Leon', 'Smith'), 74061370, 'JoLeon@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024015917 ': [('Anna', 'Fleming', 'Barnes'), 99056622, 'AnFleming@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024019220 ': [('Andrew', 'Baldwin', 'Simmons'), 63654490, 'AnBaldwin@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024016232 ': [('Donald', 'Lucero', 'French'), 79683138, 'DoLucero@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024016201 ': [('Chelsea', 'Ortiz', 'Hunter'), 98013659, 'ChOrtiz@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024011109 ': [('Lori', 'Stevens', 'Garcia'), 85485412, 'LoStevens@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024014827 ': [('Michael', 'Lucas', 'Williams'), 64469799, 'MiLucas@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024013733 ': [('Zachary', 'Khan', 'Hanson'), 67466232, 'ZaKhan@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024019806 ': [('Billy', 'Rivas', 'Miller'), 80227339, 'BiRivas@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024014917 ': [('Ryan', 'Miller', 'Wells'), 60632579, 'RyMiller@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024016132 ': [('Gina', 'Thompson', 'Briggs'), 88094563, 'GiThompson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024011990 ': [('Samuel', 'Patel', 'Petersen'), 72957368, 'SaPatel@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024019106 ': [('Matthew', 'Cunningham', 'Glover'), 74668766, 'MaCunningham@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024018306 ': [('Melissa', 'Bailey', 'Harvey'), 74794053, 'MeBailey@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024014743 ': [('John', 'Petty', 'Hall'), 61402585, 'JoPetty@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024011630 ': [('Lisa', 'Hayes', 'Thompson'), 74817547, 'LiHayes@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024017878 ': [('Mark', 'Hansen', 'Ferguson'), 60363670, 'MaHansen@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024014511 ': [('Melissa', 'Lane', 'Rosario'), 77637800, 'MeLane@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024018442 ': [('Pamela', 'Perkins', 'Wolf'), 72357395, 'PaPerkins@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024015289 ': [('Joseph', 'Young', 'Thomas'), 69239528, 'JoYoung@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024011862 ': [('Daniel', 'Williams', 'Price'), 76916539, 'DaWilliams@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024017432 ': [('Connor', 'Boyd', 'Evans'), 78509246, 'CoBoyd@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024019625 ': [('Frederick', 'Burke', 'Mendoza'), 98869126, 'FrBurke@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0] ,
' 2024014121 ': [('Kimberly', 'Murphy', 'Vasquez'), 99715681, 'KiMurphy@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024013250 ': [('Mike', 'Baker', 'Jones'), 63323686, 'MiBaker@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024011540 ': [('Amanda', 'Taylor', 'Rose'), 93086711, 'AmTaylor@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024014413 ': [('Valerie', 'Sawyer', 'Davis'), 63241539, 'VaSawyer@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024011419 ': [('Benjamin', 'Long', 'Watkins'), 92243439, 'BeLong@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024019599 ': [('Terrence', 'Chavez', 'Hughes'), 97166065, 'TeChavez@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024019061 ': [('Alexis', 'Hanna', 'Mccarthy'), 91165921, 'AlHanna@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024016983 ': [('Tammy', 'Smith', 'Walters'), 90863848, 'TaSmith@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024016015 ': [('Aaron', 'Zamora', 'Hanson'), 73529017, 'AaZamora@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024017207 ': [('Alexander', 'Graham', 'Wilson'), 86012767, 'AlGraham@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024013400 ': [('Bryce', 'Clay', 'Fernandez'), 66178996, 'BrClay@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024018464 ': [('Linda', 'Armstrong', 'Weiss'), 70596412, 'LiArmstrong@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024014529 ': [('Jeffrey', 'Christensen', 'Brown'), 65970612, 'JeChristensen@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024012903 ': [('Shane', 'Sanchez', 'Dunn'), 82451760, 'ShSanchez@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024011257 ': [('Edward', 'Cunningham', 'Benson'), 87652120, 'EdCunningham@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024015375 ': [('Aaron', 'Griffith', 'Blackwell'), 79304300, 'AaGriffith@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024019969 ': [('Joseph', 'Harris', 'Lowe'), 69477876, 'JoHarris@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024018499 ': [('Austin', 'Lewis', 'Bailey'), 95658503, 'AuLewis@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024012837 ': [('Kevin', 'Walters', 'Morales'), 96143349, 'KeWalters@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024014905 ': [('Veronica', 'Mullins', 'Stuart'), 78039038, 'VeMullins@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024018958 ': [('Daniel', 'Sanchez', 'Dixon'), 97723287, 'DaSanchez@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024011927 ': [('Catherine', 'Rogers', 'Christensen'), 90938803, 'CaRogers@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024012374 ': [('Steven', 'Martin', 'Rodriguez'), 82118066, 'StMartin@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024013800 ': [('Allen', 'Torres', 'Gilbert'), 62067273, 'AlTorres@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024016387 ': [('Christina', 'Campbell', 'Murray'), 83990021, 'ChCampbell@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Física', 0] ,
' 2024013808 ': [('Sandra', 'Wagner', 'Anderson'), 99572968, 'SaWagner@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024019002 ': [('Timothy', 'Schmidt', 'Jordan'), 75497526, 'TiSchmidt@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024014116 ': [('Donna', 'Warner', 'Berry'), 83673854, 'DoWarner@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024017284 ': [('Bryan', 'Mercer', 'Durham'), 81082901, 'BrMercer@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024014244 ': [('Keith', 'Cobb', 'Knight'), 80536959, 'KeCobb@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024019826 ': [('Andrew', 'Hernandez', 'Cain'), 97961232, 'AnHernandez@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024013735 ': [('Samuel', 'Thompson', 'Johnson'), 70711765, 'SaThompson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024019064 ': [('Robert', 'Merritt', 'Richardson'), 65078133, 'RoMerritt@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024019842 ': [('Robin', 'Santos', 'Hampton'), 73506019, 'RoSantos@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024011530 ': [('Claire', 'Villegas', 'Holt'), 95131813, 'ClVillegas@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024017894 ': [('Jeffery', 'Johnson', 'Gray'), 72643363, 'JefJohnson7@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024017163 ': [('Reginald', 'Fisher', 'Griffith'), 77261728, 'ReFisher@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024013448 ': [('Alexander', 'Walker', 'Warner'), 69561616, 'AleWalker9@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024013320 ': [('Laura', 'Wu', 'Miller'), 78827714, 'LaWu@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024018458 ': [('Elizabeth', 'Barber', 'Nelson'), 74461664, 'ElBarber@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024013083 ': [('Kenneth', 'Davis', 'Russell'), 74127849, 'KeDavis@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024018895 ': [('Angela', 'Bishop', 'Gomez'), 90247776, 'AnBishop@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024016129 ': [('Nathan', 'Archer', 'Short'), 84150470, 'NaArcher@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024016770 ': [('Robert', 'Jimenez', 'Chavez'), 87027875, 'RoJimenez@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024019135 ': [('Brian', 'Stuart', 'Dixon'), 60774223, 'BrStuart@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024015737 ': [('Stacey', 'Acosta', 'Walsh'), 69165524, 'StAcosta@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024016154 ': [('Amy', 'Townsend', 'Dawson'), 76539315, 'AmTownsend@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024017206 ': [('Jamie', 'Petty', 'Brown'), 75711375, 'JaPetty@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024018724 ': [('James', 'Duke', 'Lawson'), 65590168, 'JaDuke@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024016278 ': [('Michelle', 'Rose', 'Reid'), 81991207, 'MiRose@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Forestal', 0] ,
' 2024013654 ': [('Rhonda', 'Diaz', 'Booth'), 92822695, 'RhDiaz@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024013409 ': [('Sarah', 'Clark', 'Blackwell'), 62332182, 'SaClark@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024015265 ': [('Joanna', 'Anderson', 'Brown'), 84427597, 'JoAnderson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024018406 ': [('Bradley', 'Lopez', 'Jimenez'), 77803895, 'BrLopez@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024018616 ': [('Morgan', 'Ray', 'Herrera'), 91855850, 'MoRay@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024017379 ': [('Denise', 'Sharp', 'Davenport'), 79648472, 'DeSharp@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024014005 ': [('Walter', 'Lowe', 'Smith'), 65178559, 'WaLowe@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024013040 ': [('Alex', 'Chavez', 'Brooks'), 60797485, 'AlChavez@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024019484 ': [('Scott', 'Manning', 'Walker'), 84937328, 'ScManning@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024014769 ': [('Sara', 'Evans', 'Fox'), 71751096, 'SaEvans@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024017950 ': [('Michael', 'Robinson', 'Cox'), 60437313, 'MiRobinson@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024014049 ': [('Amanda', 'Harper', 'Mccarthy'), 68689713, 'AmHarper@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024012605 ': [('Joseph', 'Jones', 'Gonzalez'), 85189183, 'JoJones@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024018188 ': [('Ashley', 'Scott', 'Miller'), 86762933, 'AsScott@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024018439 ': [('Shannon', 'Snow', 'Webster'), 87652413, 'ShSnow@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024015505 ': [('Gary', 'Turner', 'James'), 86545895, 'GaTurner@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024019606 ': [('Charles', 'Jones', 'Wilson'), 61714619, 'ChJones@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024013642 ': [('Jose', 'Howard', 'Hanson'), 95892450, 'JoHoward@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024019026 ': [('Bryce', 'Robertson', 'Fowler'), 65955286, 'BryRobertson5@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024018746 ': [('Caleb', 'Gregory', 'Smith'), 65503412, 'CaGregory@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024019502 ': [('Kristopher', 'Proctor', 'Walker'), 76306595, 'KrProctor@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024018798 ': [('Daniel', 'Merritt', 'Smith'), 76670424, 'DaMerritt@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024019481 ': [('David', 'Parks', 'Burke'), 77751757, 'DaParks@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024019658 ': [('Rose', 'Young', 'Schmidt'), 98938539, 'RoYoung@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024018206 ': [('Sara', 'Saunders', 'Scott'), 89944114, 'SaSaunders@estudiantec.cr', 'CTCC', 'Licenciatura en Ingeniería Mecatrónica', 0] ,
' 2024018505 ': [('Nicholas', 'Ochoa', 'Lucas'), 84529357, 'NiOchoa@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024019349 ': [('Gregory', 'Perez', 'Miller'), 98202735, 'GrPerez@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024018371 ': [('Laura', 'Jones', 'Avila'), 71957347, 'LaJones@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024017809 ': [('Christopher', 'Morrison', 'Smith'), 77597904, 'ChMorrison@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024019708 ': [('Shawn', 'Jackson', 'Mcmahon'), 75386588, 'ShaJackson9@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024018296 ': [('Brenda', 'Romero', 'Gibson'), 77085234, 'BrRomero@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024019918 ': [('Nichole', 'Saunders', 'Taylor'), 60311825, 'NiSaunders@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024011955 ': [('Marcus', 'Chavez', 'Mendez'), 78799604, 'MaChavez@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024016609 ': [('Natalie', 'Carroll', 'Ali'), 98453433, 'NaCarroll@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024017110 ': [('Robert', 'Stephens', 'White'), 87455919, 'RoStephens@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024015622 ': [('Vincent', 'Morrison', 'Cox'), 76853180, 'ViMorrison@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024017892 ': [('Angela', 'Carrillo', 'Ramos'), 79981779, 'AnCarrillo@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024019411 ': [('Robert', 'Brown', 'Becker'), 88039716, 'RoBrown@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024018157 ': [('Kevin', 'Smith', 'Miller'), 77000184, 'KeSmith@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024015288 ': [('Anna', 'Cooper', 'Martin'), 77728097, 'AnCooper@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024011583 ': [('Roy', 'Hartman', 'Carpenter'), 91908952, 'RoHartman@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024011159 ': [('Daniel', 'Jarvis', 'Love'), 64490813, 'DaJarvis@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024013176 ': [('Brenda', 'Baker', 'Moore'), 67315085, 'BrBaker@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024014442 ': [('Andrew', 'Goodman', 'Gonzales'), 60780667, 'AnGoodman@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024019406 ': [('Tammy', 'Hardy', 'James'), 61371550, 'TaHardy@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024016838 ': [('Daniel', 'Hall', 'Lambert'), 67575128, 'DaHall@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024017331 ': [('Tiffany', 'Wright', 'Bailey'), 77112966, 'TiWright@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024013911 ': [('Amber', 'Ford', 'Peters'), 82392564, 'AmFord@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024018622 ': [('Rhonda', 'Molina', 'Mcdonald'), 95856346, 'RhMolina@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024012429 ': [('Daniel', 'Lowe', 'Martinez'), 78897544, 'DaLowe@estudiantec.cr', 'CTCC', 'Licenciatura en Mantenimiento Industrial', 0] ,
' 2024047333 ': [('Christopher', 'Reed', 'Hayes'), 83894887, 'ChReed@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024049554 ': [('Karen', 'Little', 'Perry'), 99353681, 'KaLittle@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024044537 ': [('Amy', 'Jackson', 'Alexander'), 88019583, 'AmJackson@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024049043 ': [('Kevin', 'Valdez', 'Moreno'), 92266010, 'KeValdez@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024045790 ': [('Jennifer', 'Zimmerman', 'Myers'), 79908877, 'JeZimmerman@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024042739 ': [('Emily', 'Pugh', 'Watson'), 61295909, 'EmPugh@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024045130 ': [('Matthew', 'Gonzales', 'Parrish'), 81137354, 'MaGonzales@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024046728 ': [('Richard', 'Higgins', 'Stewart'), 85169526, 'RiHiggins@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024046038 ': [('Scott', 'Nelson', 'Hart'), 67132534, 'ScNelson@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024046482 ': [('Daniel', 'Golden', 'Harris'), 61070222, 'DaGolden@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024041240 ': [('Rick', 'Johnson', 'Richardson'), 81696267, 'RiJohnson@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024043602 ': [('Jessica', 'Lin', 'Chambers'), 77704695, 'JeLin@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024045532 ': [('Jonathan', 'Smith', 'Donovan'), 82853707, 'JoSmith@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024042308 ': [('Evan', 'Young', 'Zuniga'), 89169564, 'EvYoung@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024049794 ': [('April', 'Davis', 'Valenzuela'), 98404245, 'ApDavis@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024043952 ': [('Ashley', 'Randolph', 'Hardy'), 62872329, 'AsRandolph@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024048293 ': [('Cynthia', 'Robinson', 'Pitts'), 81924606, 'CyRobinson@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024042733 ': [('Bruce', 'Flores', 'Castillo'), 99086601, 'BrFlores@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024041067 ': [('Andrew', 'Jones', 'Owens'), 71000703, 'AnJones@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024045195 ': [('Timothy', 'Andrews', 'Conway'), 77238105, 'TiAndrews@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024045787 ': [('James', 'Ward', 'Hernandez'), 76517779, 'JaWard@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024041637 ': [('Andrea', 'Mccoy', 'Smith'), 60930912, 'AnMccoy@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024043272 ': [('Natalie', 'Hall', 'Thomas'), 95173759, 'NaHall@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024044677 ': [('Brandon', 'Anderson', 'Pearson'), 61573834, 'BrAnderson@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024045719 ': [('Jennifer', 'Monroe', 'Harris'), 61586770, 'JeMonroe@estudiantec.cr', 'CAA', 'Bachillerato en Ingeniería en Computación', 0] ,
' 2024042256 ': [('Natalie', 'Malone', 'Long'), 68170019, 'NaMalone@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024047638 ': [('Kent', 'Hawkins', 'Guzman'), 89569083, 'KeHawkins@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024041141 ': [('Julia', 'Tucker', 'Williams'), 92031897, 'JuTucker@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024043285 ': [('Carol', 'Johnson', 'Carr'), 92227856, 'CaJohnson@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024044665 ': [('Sean', 'Barrera', 'Harmon'), 65751004, 'SeBarrera@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024044850 ': [('Tara', 'Jimenez', 'Thompson'), 99455984, 'TaJimenez@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024041308 ': [('Dawn', 'Henry', 'Simmons'), 72115203, 'DaHenry@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024045974 ': [('Timothy', 'Randall', 'Allen'), 72081963, 'TiRandall@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024049168 ': [('Francisco', 'Russell', 'Thomas'), 66031866, 'FrRussell@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024042709 ': [('Barbara', 'Brown', 'Shelton'), 80904794, 'BaBrown@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024044186 ': [('John', 'Rivera', 'Murphy'), 98182268, 'JohRivera3@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024046858 ': [('Sharon', 'Carlson', 'Bailey'), 87561685, 'ShCarlson@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024046494 ': [('Sharon', 'Lee', 'Baker'), 63874820, 'ShLee@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024049660 ': [('Chad', 'Landry', 'Johnson'), 77692773, 'ChLandry@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024047822 ': [('Lori', 'Blair', 'Mack'), 69589420, 'LoBlair@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024049637 ': [('Kaitlyn', 'Rivera', 'Warren'), 94089943, 'KaRivera@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024041056 ': [('Jennifer', 'Mahoney', 'Stevens'), 64686004, 'JeMahoney@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024046181 ': [('Alicia', 'Mckinney', 'Reyes'), 86363560, 'AlMckinney@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024042627 ': [('Kimberly', 'Farrell', 'Hardin'), 68795277, 'KimFarrell3@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024046974 ': [('Jennifer', 'Hawkins', 'Carter'), 88396184, 'JeHawkins@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024044060 ': [('Holly', 'Steele', 'Simpson'), 61543986, 'HoSteele@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024045121 ': [('Jeremiah', 'Lee', 'Watson'), 92044011, 'JeLee@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024047804 ': [('Brandon', 'Johnson', 'Castaneda'), 93134721, 'BraJohnson4@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024041261 ': [('Emily', 'Atkins', 'Hanson'), 94069438, 'EmAtkins@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
' 2024046178 ': [('Gary', 'Dillon', 'Dillon'), 85232809, 'GaDillon@estudiantec.cr', 'CAA', 'Licenciatura en Ingeniería Electrónica', 0] ,
}
diccMentores={'CTLSC': [['2023027180', ('Stacie', 'Taylor', 'Powell'), 'Bachillerato en Administración de Empresas', 'StTaylor@estudiantec.cr'], ['2023022268', ('Leslie', 'Robbins', 'Garcia'), 'Bachillerato en Gestión del Turismo Rural Sostenible', 'LeRobbins@estudiantec.cr'], ['2023023620', ('Ariel', 'Trujillo', 'Davis'), 'Bachillerato en Gestión en Sostenibilidad Turística', 'ArTrujillo@estudiantec.cr'], ['2023021783', ('Dennis', 'Tanner', 'Hensley'), 'Bachillerato en Ingeniería en Computación', 'DeTanner@estudiantec.cr'], ['2023028595', ('Christopher', 'Williams', 'Fleming'), 'Licenciatura en Ingeniería Electrónica', 'ChWilliams@estudiantec.cr'], ['2023022060', ('Lisa', 'Vang', 'Castaneda'), 'Licenciatura en Ingeniería en Agronomía', 'LiVang@estudiantec.cr'], ['2023023729', ('Vanessa', 'Williamson', 'Smith'), 'Licenciatura en Ingeniería en Producción Industrial', 'VaWilliamson@estudiantec.cr']], 'CTLSJ': [['2023033049', ('Jonathan', 'Lopez', 'Dickerson'), 'Bachillerato en Administración de Empresas', 'JoLopez@estudiantec.cr'], ['2023035141', ('Paula', 'Watts', 'Clark'), 'Bachillerato en Ingeniería en Computación', 'PaWatts@estudiantec.cr'], ['2023035984', ('Robert', 'Giles', 'Marshall'), 'Licenciatura en Arquitectura', 'RoGiles@estudiantec.cr']], 'CAL': [['2023057426', ('Julia', 'Gonzalez', 'Sanders'), 'Bachillerato en Administración de Empresas', 'JuGonzalez@estudiantec.cr'], ['2023057653', ('Marcus', 'Tanner', 'Kim'), 'Bachillerato en Ingeniería en Computación', 'MaTanner@estudiantec.cr'], ['2023056386', ('Tina', 'Collins', 'Rhodes'), 'Bachillerato en Producción Industrial,  Limón', 'TiCollins@estudiantec.cr']], 'CTCC': [['2023016134', ('Joel', 'Higgins', 'Duarte'), 'Bachillerato en Administración de Empresas', 'JoHiggins@estudiantec.cr'], ['2023018883', ('Frederick', 'Ray', 'Torres'), 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 'FrRay@estudiantec.cr'], ['2023013656', ('Cristina', 'Stevens', 'Lowery'), 'Bachillerato en Gestión del Turismo Sostenible', 'CrStevens@estudiantec.cr'], ['2023016929', ('Zachary', 'Cardenas', 'Ramirez'), 'Bachillerato en Ingeniería en Biotecnología', 'ZaCardenas@estudiantec.cr'], ['2023017535', ('Michelle', 'Wall', 'Ortiz'), 'Bachillerato en Ingeniería en Computación', 'MiWall@estudiantec.cr'], ['2023013096', ('Douglas', 'Jackson', 'Escobar'), 'Licenciatura en Administración de Tecnología de Información', 'DoJackson@estudiantec.cr'], ['2023013492', ('James', 'Rogers', 'Nichols'), 'Licenciatura en Ingeniería Agrícola', 'JaRogers@estudiantec.cr'], ['2023017427', ('Carol', 'Bates', 'Clark'), 'Licenciatura en Ingeniería Ambiental', 'CaBates@estudiantec.cr'], ['2023018784', ('Victor', 'Chambers', 'Gill'), 'Licenciatura en Ingeniería Electrónica', 'ViChambers@estudiantec.cr'], ['2023018140', ('Christopher', 'Marshall', 'Gates'), 'Licenciatura en Ingeniería en Agronegocios', 'ChMarshall@estudiantec.cr'], ['2023011145', ('Austin', 'Boyd', 'Cox'), 'Licenciatura en Ingeniería en Computadores', 'AuBoyd@estudiantec.cr'], ['2023015984', ('David', 'Martinez', 'Gonzales'), 'Licenciatura en Ingeniería en Construcción', 'DaMartinez@estudiantec.cr'], ['2023011617', ('Adam', 'Alvarez', 'Ross'), 'Licenciatura en Ingeniería en Diseño Industrial', 'AdAlvarez@estudiantec.cr'], ['2023016435', ('James', 'Sanders', 'King'), 'Licenciatura en Ingeniería en Materiales', 'JaSanders@estudiantec.cr'], ['2023015299', ('Phillip', 'Love', 'Thomas'), 'Licenciatura en Ingeniería en Producción Industrial', 'PhLove@estudiantec.cr'], ['2023012068', ('Jerry', 'Rodriguez', 'Leblanc'), 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 'JeRodriguez@estudiantec.cr'], ['2023016166', ('Patrick', 'Waller', 'Church'), 'Licenciatura en Ingeniería Física', 'PaWaller@estudiantec.cr'], ['2023016506', ('Elijah', 'Giles', 'Klein'), 'Licenciatura en Ingeniería Forestal', 'ElGiles@estudiantec.cr'], ['2023018453', ('Anna', 'Pruitt', 'Mccullough'), 'Licenciatura en Ingeniería Mecatrónica', 'AnPruitt@estudiantec.cr'], ['2023015802', ('Shannon', 'Cain', 'Houston'), 'Licenciatura en Mantenimiento Industrial', 'ShCain@estudiantec.cr']], 'CAA': [['2023041882', ('Samuel', 'Estrada', 'Reyes'), 'Bachillerato en Ingeniería en Computación', 'SaEstrada@estudiantec.cr'], ['2023049765', ('James', 'Johnson', 'Jones'), 'Licenciatura en Ingeniería Electrónica', 'JaJohnson@estudiantec.cr']]}
codigosSedes = {"CTLSC": "02", "CTLSJ": "03", "CAL": "05", "CTCC": "01", "CAA": "04"}
formato=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}$"
inicialesSedes={"Campus Tecnológico Local San Carlos": "CTLSC","Campus Tecnológico Local San José": "CTLSJ","Centro Académico de Limón": "CAL","Campus Tecnológico Central Cartago": "CTCC","Centro Académico de Alajuela": "CAA"}

def generarArchivo(estudiantes,mentores,nombre):
    encabezadosEstudiantes = ["Sede", "Carrera", "Carnet", "Nombre", "Correo", "Teléfono", "Estudiante"]
    encabezadosMentores = ["Sede", "Carrera", "Carnet", "Nombre", "Correo", "Mentor"]
    with open(f"{nombre}.csv", mode='w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(encabezadosEstudiantes) 
        for estudiante in estudiantes:
            writer.writerow(estudiante)

        writer.writerow(encabezadosMentores)

        for mentor in mentores:
            writer.writerow(mentor)  

def crearBaseDatos(diccEstudiantes,diccMentores):
    
    fecha=datetime.datetime.now().strftime("%d-%m-%Y_%H-%M")
    infoEstudiantes=[]
    infoMentores=[]
    nombre="bdIntegraTEC"+fecha
    for estudiante in diccEstudiantes.keys():
        info=[]
        info=[diccEstudiantes[estudiante][3],diccEstudiantes[estudiante][4],estudiante,diccEstudiantes[estudiante][0],diccEstudiantes[estudiante][2],diccEstudiantes[estudiante][1],True]
        infoEstudiantes.append(info)
    for sede in diccMentores.keys():
        for mentor in diccMentores[sede]:
            info=[]
            info=[sede,mentor[2],mentor[0],mentor[1],mentor[3],False]
            infoMentores.append(info)
    print(nombre)
    generarArchivo(infoEstudiantes,infoMentores,nombre)

    print("Base de datos creada con éxito.")
        

def obtenerCarreras(estructura):
    carreras=[]
    for sede in estructura.keys():
        for carrera in estructura[sede]:
            if carrera[0] not in carreras:
                carreras.append(carrera[0])
    return carreras

def generarReporteMentor(diccMentores, diccEstudiantes):
    with open("Reporte por mentor.html", "w", encoding="utf-8") as reporte:
        reporte.write('''<html>
                           <head>
                               <title>Reporte por mentor</title>
                           </head>
                           <body>
                               <h1>Reporte por mentor.</h1>''')

        for sede, mentores in diccMentores.items():
            reporte.write(f'<h2>Sede: {sede}</h2>')

            for mentor in mentores:
                mentor_nombre = mentor[1][0]
                mentor_carnet = mentor[0]
                reporte.write(f'<h3>Mentor: {mentor_nombre}</h3>')

                estudiantes_asignados = []
                contador = 1  

                for carnet, estudiante_info in diccEstudiantes.items():
                    if estudiante_info[-1] == mentor_carnet:
                        estudiantes_asignados.append((carnet, estudiante_info[0]))

                if estudiantes_asignados:
                    for carnet, nombre_estudiante in estudiantes_asignados:
                        reporte.write(f'<li>{contador}. {carnet} - {nombre_estudiante}</li>')
                        contador += 1
                else:
                    reporte.write('<p>No hay estudiantes asignados a este mentor.</p>')

        reporte.write('''</body>
                        </html>''')

    print("Reporte por mentor generado con éxito.")

def extraerInfoCarrera(diccEstudiantes,lista):
    info=[]
    for estudiante in diccEstudiantes.keys():
        for i in lista:
            if estudiante==i:
                info.append(diccEstudiantes[estudiante])
                continue
    return info

def generarReporteCarrera(estructura, diccEstudiantes, carrera):
    with open("Reporte por carrera.html", "w", encoding="utf-8") as reporte:
        reporte.write('''<html>
                           <head>
                               <title>Reporte por carrera</title>
                           </head>
                           <body>
                               <h1>Reporte por carrera.</h1>
                               <h2>{}</h2>
                               <table border='1'>
                                   <tr bgcolor="0C9208">
                                       <th style="color: white;">Información de estudiantes</th>
                                   </tr>\n'''.format(carrera))

        i = 1

        for sede in estructura.keys():
            info = extraerInfoCarrera(diccEstudiantes, extraerEstudiantesSedeCarrera(diccEstudiantes, sede, carrera))
            for infoCompleta in info:
                infoEstudiante = " - ".join(map(str, infoCompleta))
                reporte.write(f'''<tr  style="background-color: #D7BCE9;">
                                    <td align="center">{i}. {infoEstudiante}</td>
                                </tr>\n''')
                i += 1  
            
        reporte.write('''</table>
                        </body>
                        </html>''')

    print("Reporte por carrera generado con éxito.")

def extraerInformacionSede(diccEstudiantes,lista):
    info=[]
    for estudiante in diccEstudiantes.keys():
        for i in lista:
            if estudiante==i:
                info.append(diccEstudiantes[estudiante])
                continue
    return info

def generarReporteSede(estructura, diccEstudiantes, inicialesSedes):
    with open("Reporte por sede.html", "w", encoding="utf-8") as reporte:
        reporte.write('''<html>
                           <head>
                               <title>Reporte por sede</title>
                           </head>
                           <body>
                               <h1>Reporte por sede.</h1>''')
        for sede in estructura.keys():
            sede_nombre = obtener_clave_por_valor(inicialesSedes, sede)
            reporte.write(f'''<h2>{sede_nombre}</h2>
                            <table border='1'>
                                   <tr bgcolor="0C9208">
                                       <th style="color: white;">Carrera</th>
                                       <th style="color: white;">Información de estudiantes</th>
                                   </tr>\n''')
            for pos, carrera in enumerate(estructura[sede]):
                estudiantes = extraerInformacionSede(diccEstudiantes,extraerEstudiantesSedeCarrera(diccEstudiantes, sede, carrera[0]))
                reporte.write(f'''<tr  style="background-color: #D7BCE9;">
                                    <td align="center">{carrera[0]}</td>
                                    <td align="center">{estudiantes}</td>
                                </tr>\n''')
            reporte.write('''</table>\n''')
        reporte.write('''</body>
                            </html>''')

    print("Reporte por sede generado con éxito.")

def extraerMentoresSedeCarrera(diccMentores, sede, carrera):
    mentoresCarrera = []
    for mentor in diccMentores[sede]:
        carreraMentor = mentor[2]
        if carreraMentor == carrera:
            mentoresCarrera.append(mentor)
    return mentoresCarrera

def extraerEstudiantesSedeCarrera(diccEstudiantes, sede, carrera):
    estudiantesCarreraSede = []
    for estudiante in diccEstudiantes.keys():
        sedeEstudiante = diccEstudiantes[estudiante][3]  
        carreraEstudiante = diccEstudiantes[estudiante][4] 
        if sedeEstudiante == sede and carreraEstudiante == carrera:
            estudiantesCarreraSede.append(estudiante)
    return estudiantesCarreraSede

def asignarMentores(diccEstudiantes, diccMentores, estructura):
    for sede in estructura.keys():
        for carrera in estructura[sede]:
            estudiantesSedeCarrera = extraerEstudiantesSedeCarrera(diccEstudiantes, sede, carrera[0])
            mentores = extraerMentoresSedeCarrera(diccMentores, sede, carrera[0])
            cantidadEstudiantes = len(estudiantesSedeCarrera)
            cantidadMentores = len(mentores)
            if cantidadMentores == 0:
                print("No hay mentores para la carrera", carrera[0], "en la sede", sede)
                continue
            estudiantesMentor = cantidadEstudiantes // cantidadMentores
            estudiantesSobrantes = cantidadEstudiantes % cantidadMentores
            i = 0
            for mentor in mentores:
                asignarEstudiantes = estudiantesMentor
                if estudiantesSobrantes > 0:
                    asignarEstudiantes += 1
                    estudiantesSobrantes -= 1
                for i in range(asignarEstudiantes):
                    
                    estudiante = estudiantesSedeCarrera[i]
                    diccEstudiantes[estudiante][5] = mentor[0] 
                    i += 1

    return diccEstudiantes

def generarCarnetsMentores(estructuraCarrerasCantidad,codigosSedes,totalCarnets,totalNumeros,totalCorreos,diccMentores):
    for sede in estructuraCarrerasCantidad.keys():
        listaMentores=[]
        for i,carrera in enumerate(estructuraCarrerasCantidad[sede]):
                cantidadMentores = round(estructuraCarrerasCantidad[sede][i][1]*0.05)
                

                for j in range(cantidadMentores):
                    nuevoCarnet = None

                    while nuevoCarnet is None or nuevoCarnet in totalCarnets:
                        nuevoCarnet = generarNumCarnet(2,codigosSedes[sede])

                    totalCarnets.append(nuevoCarnet)

                    nombreCompleto , telefono , correo = generarDatos(1,"","")

                    while correo in totalCorreos:
                        correo = generarDatos(3,nombreCompleto[0][1:],nombreCompleto[1])
                    totalCorreos.append(correo)

                    listaMentores.append([nuevoCarnet,nombreCompleto, carrera[0], correo])
                    
        diccMentores[sede] = listaMentores
                    
    return diccMentores

def obtenerSedesCarreras(inicialesSedes):
    carrerasSede = {}
    resp = requests.get(urlSedes)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "html.parser")
        carrerasPorSede = soup.find_all("div", class_="view-content")[0]
        for sede in carrerasPorSede.find_all("div", class_="group"):
            nombreSede=sede.find("a").text
            lugar=inicialesSedes.get(nombreSede)
            carrerasSede[lugar]=[]
            for carrera in sede.find_all("div", class_="title"):
               nombre_carrera = carrera.find("a").text
               carrerasSede[lugar].append(nombre_carrera)
    return carrerasSede

def generarNumCarnet(gen,sede):
    numRandom = random.randint(1000, 9999)
    if gen == 1:
        nuevoCarnet = "2024" + sede + str(numRandom)
    else:
        nuevoCarnet = "2023" + sede + str(numRandom)
    return nuevoCarnet

def generarDatos(opcion,pnombre,papellido1):
    if opcion == 1:
        fake=Faker()
        nombre = fake.first_name()
        apellido1 = fake.last_name()
        apellido2 = fake.last_name()
        nombreCompleto = (nombre, apellido1, apellido2)
        telefono = random.randint(60000000, 99999999)
        correo = nombre[:2]+apellido1+"@estudiantec.cr"
        return nombreCompleto,telefono,correo
    elif opcion == 2:
        return random.randint(60000000, 99999999)
    elif opcion == 3:
        num=random.randint(1,9)
        return pnombre[:3]+papellido1+str(num)+"@estudiantec.cr"
        
def generarCarnetsEstudiantes(totalAdmitidos, estructuraCarrerasCantidad,codigosSedes,totalCarnets,totalNumeros,totalCorreos,diccEstudiantes):
    
    for sede in totalAdmitidos.keys():
        print("generando carnets de estudiantes")
        for i,carrera in enumerate(estructuraCarrerasCantidad[sede]):
            
            cantidad_admitidos = estructuraCarrerasCantidad[sede][i][1]

            for _ in range(cantidad_admitidos):
                nuevoCarnet = None
                
                while nuevoCarnet is None or nuevoCarnet in totalCarnets:
                    nuevoCarnet = generarNumCarnet(1,codigosSedes[sede])

                totalCarnets.append(nuevoCarnet)

                nombreCompleto , telefono , correo = generarDatos(1,"","")
                
                while telefono in totalNumeros:
                    telefono = generarDatos(2,"","")
                totalNumeros.append(telefono)

                while correo in totalCorreos:
                    correo = generarDatos(3,nombreCompleto[0],nombreCompleto[1])
                totalCorreos.append(correo)


                diccEstudiantes[nuevoCarnet] = [nombreCompleto, telefono, correo, sede, carrera[0],0]

    return diccEstudiantes

def validarCorreo(correo):
    if re.match(formato,correo):
        return True
    else:
        return False

def imprimir_diccionario(diccionario):
    print("{")
    for clave, valor in diccionario.items():
        print("'",clave,"'" ":", valor,",")
    print("}")        

def obtener_clave_por_valor(diccionario, valor_buscado):
    for clave, valor in diccionario.items():
        if valor == valor_buscado:
            return clave
    # Si no se encuentra el valor, puedes devolver None u otro valor predeterminado.
    return None

#info={"ctaa":[["Ingeniería en Computadores",0],["Ingeniería en Computación",5100],["Ingeniería en Computación con Énfasis en Sistemas de Información Empresarial,",0]],}
#print(info["ctaa"][1][1])
#estructura=generarCarnetsEstudiantes(totalAdmitidos, estructura,codigosSedes,[],[],[],{})
#imprimir_diccionario(estructura)
#print(generarCarnetsMentores(estructura,codigosSedes,[],[],[],{}))
#estructura=generarCarnetsMentores(estructura,codigosSedes,[],[],[],{})
#imprimir_diccionario(estructura)
#diccEstudiantes=asignarMentores(diccEstudiantes,diccMentores,estructura)
#imprimir_diccionario(diccEstudiantes)
#imprimir_diccionario(asignarMentores(diccEstudiantes,diccMentores,estructura))
#generarReporteSede(estructura,diccEstudiantes,inicialesSedes)
#generarReporteCarrera(estructura,diccEstudiantes,"Bachillerato en Ingeniería en Computación")
#diccEstudiantes=asignarMentores(diccEstudiantes,diccMentores,estructura)
#generarReporteMentor(diccMentores,diccEstudiantes,estructura)

crearBaseDatos(diccEstudiantes,diccMentores)
#crearBaseDatosTxt(diccEstudiantes, diccMentores)


