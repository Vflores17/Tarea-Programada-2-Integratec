from tkinter import * 
from funcionesProyecto2 import *
from tkinter import messagebox
import random

ventana = Tk()
totalAdmitidos={"CTLSC":175,"CTLSJ":75,"CAL":75,"CTCC":625,"CAA":50}
estructuraCarrerasCantidad={'CTLSC': [['Bachillerato en Administración de Empresas', 0], ['Bachillerato en Gestión del Turismo Rural Sostenible', 0], ['Bachillerato en Gestión en Sostenibilidad Turística', 0], ['Bachillerato en Ingeniería en Computación', 0], ['Licenciatura en Ingeniería Electrónica', 0], ['Licenciatura en Ingeniería en Agronomía', 0], ['Licenciatura en Ingeniería en Producción Industrial', 0]], 'CTLSJ': [['Bachillerato en Administración de Empresas', 0], ['Bachillerato en Ingeniería en Computación', 0], ['Licenciatura en Arquitectura', 0]], 'CAL': [['Bachillerato en Administración de Empresas', 0], ['Bachillerato en Ingeniería en Computación', 0], ['Bachillerato en Producción Industrial,  Limón', 0]], 'CTCC': [['Bachillerato en Administración de Empresas', 0], ['Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0], ['Bachillerato en Gestión del Turismo Sostenible', 0], ['Bachillerato en Ingeniería en Biotecnología', 0], ['Bachillerato en Ingeniería en Computación', 0], ['Licenciatura en Administración de Tecnología de Información', 0], ['Licenciatura en Ingeniería Agrícola', 0], ['Licenciatura en Ingeniería Ambiental', 0], ['Licenciatura en Ingeniería Electrónica', 0], ['Licenciatura en Ingeniería en Agronegocios', 0], ['Licenciatura en Ingeniería en Computadores', 0], ['Licenciatura en Ingeniería en Construcción', 0], ['Licenciatura en Ingeniería en Diseño Industrial', 0], ['Licenciatura en Ingeniería en Materiales', 0], ['Licenciatura en Ingeniería en Producción Industrial', 0], ['Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0], ['Licenciatura en Ingeniería Física', 0], ['Licenciatura en Ingeniería Forestal', 0], ['Licenciatura en Ingeniería Mecatrónica', 0], ['Licenciatura en Mantenimiento Industrial', 0]], 'CAA': [['Bachillerato en Ingeniería en Computación', 0], ['Licenciatura en Ingeniería Electrónica', 0]]}
#estructuraCarrerasCantidad={'CTLSC': [['Bachillerato en Administración de Empresas', 25], ['Bachillerato en Gestión del Turismo Rural Sostenible', 25], ['Bachillerato en Gestión en Sostenibilidad Turística', 25], ['Bachillerato en Ingeniería en Computación', 25], ['Licenciatura en Ingeniería Electrónica', 25], ['Licenciatura en Ingeniería en Agronomía', 25], ['Licenciatura en Ingeniería en Producción Industrial', 25]], 'CTLSJ': [['Bachillerato en Administración de Empresas', 25], ['Bachillerato en Ingeniería en Computación', 25], ['Licenciatura en Arquitectura', 25]], 'CAL': [['Bachillerato en Administración de Empresas', 25], ['Bachillerato en Ingeniería en Computación', 25], ['Bachillerato en Producción Industrial,  Limón', 25]], 'CTCC': [['Bachillerato en Administración de Empresas', 25], ['Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 25], ['Bachillerato en Gestión del Turismo Sostenible', 25], ['Bachillerato en Ingeniería en Biotecnología', 25], ['Bachillerato en Ingeniería en Computación', 25], ['Licenciatura en Administración de Tecnología de Información', 25], ['Licenciatura en Ingeniería Agrícola', 25], ['Licenciatura en Ingeniería Ambiental', 25], ['Licenciatura en Ingeniería Electrónica', 25], ['Licenciatura en Ingeniería en Agronegocios', 25], ['Licenciatura en Ingeniería en Computadores', 25], ['Licenciatura en Ingeniería en Construcción', 25], ['Licenciatura en Ingeniería en Diseño Industrial', 25], ['Licenciatura en Ingeniería en Materiales', 25], ['Licenciatura en Ingeniería en Producción Industrial', 25], ['Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 25], ['Licenciatura en Ingeniería Física', 25], ['Licenciatura en Ingeniería Forestal', 25], ['Licenciatura en Ingeniería Mecatrónica', 25], ['Licenciatura en Mantenimiento Industrial', 25]], 'CAA': [['Bachillerato en Ingeniería en Computación', 25], ['Licenciatura en Ingeniería Electrónica', 25]]}

totalCarnets={}
codigosSedes = {"CTLSC": "02", "CTLSJ": "03", "CAL": "05", "CTCC": "01", "CAA": "04"}
totalCarnets = ["2024022970","2024022672","2023025459","2023022410"]
totalNumeros = [67487497,70797830,60703107]
totalCorreos = ["JeWilliams@estudiantec.cr","AlHernandez@estudiantec.cr"]
diccEstudiantes = {'2024022970': [('Jennifer', 'Williams', 'Sanford'), 67487497, 'JeWilliams@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024022672': [('Alex', 'Hernandez', 'Thomas'), 70797830, 'AlHernandez@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024025981': [('Robert', 'Osborn', 'Perez'), 94183600, 'RoOsborn@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024029917': [('Michael', 'Daniels', 'Wells'), 66454739, 'MiDaniels@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024026809': [('Katrina', 'Young', 'Martinez'), 74895153, 'KaYoung@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024028372': [('Angelica', 'Page', 'Moore'), 78615930, 'AnPage@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024021388': [('Stephen', 'Drake', 'Morrison'), 93166120, 'StDrake@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024029720': [('Linda', 'Kramer', 'Moreno'), 96535276, 'LiKramer@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024026517': [('Janice', 'Parker', 'Ryan'), 72856719, 'JaParker@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024023979': [('Rebecca', 'Moore', 'Lopez'), 88273329, 'ReMoore@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024029839': [('Frances', 'Anderson', 'Barnes'), 97274319, 'FrAnderson@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024025607': [('Brittany', 'Hall', 'Peterson'), 88600707, 'BrHall@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024023569': [('Monica', 'Conner', 'Smith'), 71102211, 'MoConner@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024026703': [('Taylor', 'Rowe', 'Anderson'), 72788361, 'TaRowe@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024023420': [('Ashley', 'Brewer', 'Grimes'), 72665557, 'AsBrewer@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024023986': [('Michael', 'Castillo', 'Ochoa'), 82018631, 'MiCastillo@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024021896': [('Jessica', 'Roth', 'Harris'), 64183920, 'JeRoth@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024024735': [('Nathan', 'Maxwell', 'Johnson'), 69428909, 'NaMaxwell@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024025110': [('Sarah', 'Miller', 'Mcdonald'), 89574356, 'SaMiller@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024021192': [('Shannon', 'Moore', 'Graham'), 86624670, 'ShMoore@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024021431': [('Rebecca', 'Pennington', 'Jones'), 74716128, 'RePennington@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024021700': [('Jason', 'Wade', 'Gonzalez'), 90259856, 'JaWade@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024028698': [('Allison', 'Collier', 'Ferguson'), 84058359, 'AlCollier@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024025335': [('Taylor', 'Johnson', 'Berger'), 89375073, 'TaJohnson@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024025325': [('Cesar', 'Brown', 'Huang'), 85673797, 'CeBrown@estudiantec.cr', 'CTLSC', 'Bachillerato en Administración de Empresas', 0], '2024027224': [('James', 'Drake', 'Randall'), 70917352, 'JaDrake@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0], '2024027849': [('Valerie', 'Torres', 'Matthews'), 81716268, 'VaTorres@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0], '2024028096': [('Bryan', 'Love', 'Clark'), 90792230, 'BrLove@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0], '2024024365': [('Amanda', 'Ray', 'Jimenez'), 79488473, 'AmRay@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0], '2024023548': [('Jeremy', 'Smith', 'Dawson'), 65845541, 'JeSmith@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0], '2024029128': [('Ray', 'Ford', 'Salinas'), 86379667, 'RaFord@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0], '2024027182': [('Darius', 'Welch', 'Berry'), 67153806, 'DaWelch@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0], '2024025078': [('Richard', 'Dorsey', 'Green'), 95302980, 'RiDorsey@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0], '2024023877': [('Michael', 'Day', 'Nichols'), 80144835, 'MiDay@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0], '2024023628': [('Jose', 'Sampson', 'Stewart'), 76166078, 'JoSampson@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0], '2024023170': [('Michael', 'Mitchell', 'Green'), 82997414, 'MiMitchell@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0], '2024028448': [('Daniel', 'Johnson', 'Wood'), 87039656, 'DaJohnson@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0], '2024024461': [('Carla', 'Mann', 'Williams'), 84272963, 'CaMann@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0], '2024023984': [('Elizabeth', 'Hale', 'Rhodes'), 79377648, 'ElHale@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0], '2024023217': [('Lisa', 'Diaz', 'Lewis'), 72478480, 'LiDiaz@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0], '2024027502': [('Lisa', 'Yang', 'Wilson'), 86573648, 'LiYang@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0], '2024029960': [('Amber', 'Ramirez', 'Price'), 79447395, 'AmRamirez@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0], '2024029414': [('Tasha', 'Smith', 'Mitchell'), 79599852, 'TaSmith@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión del Turismo Rural Sostenible', 0], '2024024681': [('April', 'Potter', 'Cox'), 82676145, 'ApPotter@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0], '2024028962': [('Sean', 'Ford', 'Rivers'), 71261956, 'SeFord@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0], '2024024725': [('Thomas', 'Jackson', 'Harmon'), 73476936, 'ThJackson@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0], '2024024758': [('Stephanie', 'Lopez', 'Washington'), 74038317, 'StLopez@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0], '2024022410': [('Jeffrey', 'Conrad', 'Smith'), 95496522, 'JeConrad@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0], '2024025861': [('Jason', 'Williams', 'Lewis'), 78065700, 'JaWilliams@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0], '2024021241': [('Robert', 'Palmer', 'Ramirez'), 73591196, 'RoPalmer@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0], '2024022469': [('Nicholas', 'Brown', 'Anderson'), 92580113, 'NiBrown@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0], '2024025892': [('Gabriel', 'Ryan', 'Scott'), 85296757, 'GaRyan@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0], '2024023822': [('Amanda', 'Davis', 'Gibson'), 75367800, 'AmDavis@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0], '2024024174': [('Charles', 'Gaines', 'Oliver'), 75084089, 'ChGaines@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0], '2024027971': [('Anthony', 'Smith', 'Wilson'), 88059492, 'AnSmith@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0], '2024025491': [('Julie', 'Carey', 'Cook'), 78385520, 'JuCarey@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0], '2024026455': [('Christine', 'Dean', 'Mathews'), 61050288, 'ChDean@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0], '2024028964': [('Nicholas', 'Gonzalez', 'White'), 62132903, 'NiGonzalez@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0], '2024025914': [('April', 'Hall', 'Harrington'), 94170501, 'ApHall@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0], '2024023748': [('Justin', 'White', 'Nunez'), 66672404, 'JuWhite@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0], '2024024428': [('Amy', 'Howell', 'Valdez'), 78703040, 'AmHowell@estudiantec.cr', 'CTLSC', 'Bachillerato en Gestión en Sostenibilidad Turística', 0], '2024022504': [('Kevin', 'Townsend', 'Hunter'), 83026861, 'KeTownsend@estudiantec.cr', 'CTLSC', 'Bachillerato en Ingeniería en Computación',0]}
diccMentores={'CTLSC': [['2023025459', ('Lori', 'Bennett', 'Thompson'), 'Bachillerato en Administración de Empresas', 'LoBennett@estudiantec.cr'], ['2023022410', ('Elizabeth', 'Johnson', 'Mahoney'), 'Bachillerato en Gestión del Turismo Rural Sostenible', 'ElJohnson@estudiantec.cr'], ['2023028425', ('Kyle', 'Smith', 'Donaldson'), 'Bachillerato en Gestión en Sostenibilidad Turística', 'KySmith@estudiantec.cr'], ['2023023592', ('Matthew', 'Gill', 'Thompson'), 'Bachillerato en Ingeniería en Computación', 'MaGill@estudiantec.cr'], ['2023025136', ('Melissa', 'Stewart', 'Parsons'), 'Licenciatura en Ingeniería Electrónica', 'MeStewart@estudiantec.cr'], ['2023027333', ('Tyler', 'Kim', 'Lang'), 'Licenciatura en Ingeniería en Agronomía', 'TyKim@estudiantec.cr'], ['2023024468', ('Michelle', 'Pearson', 'Franklin'), 'Licenciatura en Ingeniería en Producción Industrial', 'MiPearson@estudiantec.cr'], ['2023023511', ('David', 'Lee', 'Porter'), 'Licenciatura en Ingeniería en Producción Industrial', 'aviLee7@estudiantec.cr'], ['2023028709', ('Mary', 'Long', 'Roberts'), 'Licenciatura en Ingeniería en Producción Industrial', 'MaLong@estudiantec.cr'], ['2023027959', ('Michael', 'Moreno', 'Edwards'), 'Licenciatura en Ingeniería en Producción Industrial', 'MiMoreno@estudiantec.cr']], 'CTLSJ': [['2023039623', ('Allison', 'Boone', 'Bradley'), 'Bachillerato en Administración de Empresas', 'AlBoone@estudiantec.cr'], ['2023036377', ('Valerie', 'Dean', 'Brown'), 'Licenciatura en Arquitectura', 'VaDean@estudiantec.cr'], ['2023031236', ('Ricardo', 'Vance', 'Gomez'), 'Licenciatura en Arquitectura', 'RiVance@estudiantec.cr'], ['2023034999', ('Candace', 'Rios', 'Murray'), 'Licenciatura en Arquitectura', 'CaRios@estudiantec.cr']], 'CAL': [['2023059806', ('Stephen', 'Chen', 'Sanders'), 'Bachillerato en Producción Industrial,  Limón', 'StChen@estudiantec.cr'], ['2023054982', ('William', 'Moreno', 'Hoffman'), 'Bachillerato en Producción Industrial,  Limón', 'WiMoreno@estudiantec.cr'], ['2023054090', ('Rebekah', 'Moore', 'Ruiz'), 'Bachillerato en Producción Industrial,  Limón', 'ebeMoore3@estudiantec.cr']], 'CTCC': [['2023018892', ('Thomas', 'Pierce', 'Barnes'), 'Bachillerato en Administración de Empresas', 'ThPierce@estudiantec.cr'], ['2023016918', ('Aaron', 'Carlson', 'Smith'), 'Bachillerato en Administración de Empresas', 'AaCarlson@estudiantec.cr'], ['2023015182', ('Daniel', 'Craig', 'Thomas'), 'Bachillerato en Administración de Empresas', 'DaCraig@estudiantec.cr'], ['2023018554', ('Hannah', 'Lopez', 'Jones'), 'Bachillerato en Administración de Empresas', 'HaLopez@estudiantec.cr'], ['2023019124', ('Allison', 'Davis', 'Brock'), 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 'AlDavis@estudiantec.cr'], ['2023013943', ('Alisha', 'Flores', 'Hutchinson'), 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 'AlFlores@estudiantec.cr'], ['2023011064', ('Alexis', 'Henderson', 'Perez'), 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 'AlHenderson@estudiantec.cr'], ['2023015340', ('Harold', 'Ramirez', 'Blevins'), 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 'HaRamirez@estudiantec.cr'], ['2023011803', ('Warren', 'Cox', 'Atkinson'), 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 'WaCox@estudiantec.cr'], ['2023015080', ('Robert', 'Lang', 'Watson'), 'Bachillerato en Gestión del Turismo Sostenible', 'RoLang@estudiantec.cr'], ['2023015830', ('William', 'Smith', 'Nguyen'), 'Bachillerato en Gestión del Turismo Sostenible', 'WiSmith@estudiantec.cr'], ['2023016843', ('Paul', 'Rivera', 'Hinton'), 'Bachillerato en Gestión del Turismo Sostenible', 'PaRivera@estudiantec.cr'], ['2023015456', ('Scott', 'Barnes', 'Rodriguez'), 'Bachillerato en Gestión del Turismo Sostenible', 'ScBarnes@estudiantec.cr'], ['2023011208', ('Lisa', 'Tate', 'Montgomery'), 'Bachillerato en Gestión del Turismo Sostenible', 'LiTate@estudiantec.cr'], ['2023018510', ('Molly', 'Baker', 'Barnes'), 'Bachillerato en Ingeniería en Biotecnología', 'MoBaker@estudiantec.cr'], ['2023018637', ('Tyler', 'Knox', 'Davis'), 'Bachillerato en Ingeniería en Biotecnología', 'TyKnox@estudiantec.cr'], ['2023016951', ('Cynthia', 'Green', 'Turner'), 'Bachillerato en Ingeniería en Computación', 'CyGreen@estudiantec.cr'], ['2023018116', ('Daniel', 'Mcbride', 'Franklin'), 'Bachillerato en Ingeniería en Computación', 'DaMcbride@estudiantec.cr'], ['2023018972', ('William', 'Thomas', 'Rosales'), 'Licenciatura en Administración de Tecnología de Información', 'WiThomas@estudiantec.cr'], ['2023011120', ('Peter', 'Murphy', 'Lee'), 'Licenciatura en Administración de Tecnología de Información', 'PeMurphy@estudiantec.cr'], ['2023011204', ('Jenna', 'Conrad', 'Smith'), 'Licenciatura en Ingeniería Agrícola', 'ennConrad6@estudiantec.cr'], ['2023013254', ('Melissa', 'Mullins', 'Weber'), 'Licenciatura en Ingeniería Ambiental', 'MeMullins@estudiantec.cr'], ['2023011461', ('Patrick', 'Butler', 'Floyd'), 'Licenciatura en Ingeniería Electrónica', 'PaButler@estudiantec.cr'], ['2023016241', ('Paul', 'Powell', 'Mcdaniel'), 'Licenciatura en Ingeniería en Agronegocios', 'PaPowell@estudiantec.cr'], ['2023017977', ('Penny', 'Martin', 'Hernandez'), 'Licenciatura en Ingeniería en Computadores', 'PeMartin@estudiantec.cr'], ['2023019405', ('Maria', 'Compton', 'Morris'), 'Licenciatura en Ingeniería en Construcción', 'MaCompton@estudiantec.cr'], ['2023019499', ('Paul', 'Chavez', 'Parker'), 'Licenciatura en Ingeniería en Materiales', 'PaChavez@estudiantec.cr'], ['2023015607', ('Carol', 'Wilson', 'Brown'), 'Licenciatura en Ingeniería en Producción Industrial', 'CaWilson@estudiantec.cr'], ['2023015444', ('Gloria', 'Taylor', 'Smith'), 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 'GlTaylor@estudiantec.cr'], ['2023015687', ('Eugene', 'Franco', 'Jones'), 'Licenciatura en Mantenimiento Industrial', 'EuFranco@estudiantec.cr']], 'CAA': [['2023044067', ('Anthony', 'Rivera', 'Patterson'), 'Licenciatura en Ingeniería Electrónica', 'AnRivera@estudiantec.cr'], ['2023048919', ('Jason', 'Norton', 'Lewis'), 'Licenciatura en Ingeniería Electrónica', 'JaNorton@estudiantec.cr']]}
carnet=""
inicialesSedes={"Campus Tecnológico Local San Carlos": "CTLSC","Campus Tecnológico Local San José": "CTLSJ","Centro Académico de Limón": "CAL","Campus Tecnológico Central Cartago": "CTCC","Centro Académico de Alajuela": "CAA"}
    

def opcionGenerarReportes():

    def opcionReporteMentor():
        pass

    def opcionReporteCarrera():
        pass

    def opcionReporteSede():
        pass

    def cerrarVentanaReportes():
        ventanaReportes.destroy()
        ventana.deiconify()

    ventanaReportes= tk.Toplevel(ventana)
    ventanaReportes.title("Ventana de actualización de información.")
    ventanaReportes.geometry("550x300")
    ventanaReportes.config(bg="lightblue")
    ventana.withdraw()

    #Texto en la ventana
    label = tk.Label(ventanaReportes, text="Ventana para actualizar información de los estudiantes.")
    label.config(fg="green", bg="lightgrey", font=("Verdana", 12))
    label.place(x=25, y=10)

    #Botones
    botonVolver = tk.Button(ventanaReportes, text="Volver",font=("Verdana", 10),bg="red",command=cerrarVentanaReportes,fg="white")
    botonVolver.place(x=490, y=265)

    #Menu desplegable
    menu = tk.Menu(ventanaReportes)
    opciones = tk.Menu(menu,tearoff=0)
    opciones.add_command(label="Reporte por sede",command=opcionReporteSede)
    opciones.add_command(label="Reporte por carrera",command=opcionReporteCarrera)
    opciones.add_command(label="Reporte por Mentor",command=opcionReporteMentor)


    menu.add_cascade(label="Opciones para actualiar información", menu=opciones)
    ventanaReportes.config(menu=menu)

def opcionActualizarEstudiante():


    def actualizarInfo(ventanaActualizarNombre,cajaTexto,seccion):
        global carnet
        info=cajaTexto.get()
        if len(info)>0 and seccion>=0 and seccion <=2 :
            nombreCompleto=list(diccEstudiantes[carnet][0])
            if seccion == 0:
                nombreCompleto[0]=info
            elif seccion == 1:
                nombreCompleto[1]=info
            elif seccion == 2:
                nombreCompleto[2]=info
            nombreCompleto=tuple(nombreCompleto)
            diccEstudiantes[carnet][0]=nombreCompleto
            ventanaActualizarNombre.destroy()
        
        elif len(info)>0 and seccion==3:
            global totalNumeros
            try:
                if info.isdigit() and len(info)==8:
                    if int(info) not in totalNumeros:
                        diccEstudiantes[carnet][1]=int(info)
                        ventanaActualizarNombre.destroy()
                    else:
                        messagebox.showerror("Error", "El número ingresado ya existe.")
                        cajaTexto.delete(0,END)
                else:
                    messagebox.showerror("Error", "El número ingresado no tiene el formato correcto.") 
                    cajaTexto.delete(0,END)
            except:
                messagebox.showerror("Error", "El número ingresado no es válido.")  
                cajaTexto.delete(0,END)
        elif len(info)>0 and seccion==4:
            global totalCorreos
            if validarCorreo(info):
                if info not in totalCorreos:
                    diccEstudiantes[carnet][2]=info
                    ventanaActualizarNombre.destroy()
                else:
                    messagebox.showerror("Error", "El correo ingresado ya existe.")
                    cajaTexto.delete(0,END)
            else:
                messagebox.showerror("Error", "El correo ingresado no tiene el formato correcto.")
                cajaTexto.delete(0,END)    
        else:
            messagebox.showerror("Error", "La información ingresada no es válida.")
            cajaTexto.delete(0,END)
        if carnet[:4]=="2024":
                    mostrarInfoEstudiante(carnet)
        else:
            mostrarInfoMentor(carnet)

    def habilitarOpciones():
        opciones.entryconfig("Actualizar nombre", state=NORMAL)
        opciones.entryconfig("Actualizar primer apellido", state=NORMAL)
        opciones.entryconfig("Actualizar segundo apellido", state=NORMAL)
        opciones.entryconfig("Actualizar teléfono", state=NORMAL)
        opciones.entryconfig("Actualizar correo", state=NORMAL)


    def opcionActualizarCorreo():
        ventanaActualizarNombre=tk.Toplevel(ventanaActualizarInfo)
        ventanaActualizarNombre.title("Ingresa el nuevo correo a registrar.")
        ventanaActualizarNombre.geometry("400x150")
        ventanaActualizarNombre.config(bg="lightblue")
        cajaTexto = tk.Entry(ventanaActualizarNombre,width=30)
        cajaTexto.place(x=110, y=50)
        botonAceptar = tk.Button(ventanaActualizarNombre, text="Actualizar",font=("Verdana", 10),bg="green",command=lambda:actualizarInfo(ventanaActualizarNombre,cajaTexto,4),fg="white")
        botonAceptar.place(x=150, y=100)

    def opcionActualizarTelefono():
        ventanaActualizarNombre=tk.Toplevel(ventanaActualizarInfo)
        ventanaActualizarNombre.title("Ingresa el nuevo número a registrar.")
        ventanaActualizarNombre.geometry("400x150")
        ventanaActualizarNombre.config(bg="lightblue")
        cajaTexto = tk.Entry(ventanaActualizarNombre)
        cajaTexto.place(x=100, y=50)
        botonAceptar = tk.Button(ventanaActualizarNombre, text="Actualizar",font=("Verdana", 10),bg="green",command=lambda:actualizarInfo(ventanaActualizarNombre,cajaTexto,3),fg="white")
        botonAceptar.place(x=150, y=100)

    def opcionActualizarApellido(pos):
        ventanaActualizarNombre=tk.Toplevel(ventanaActualizarInfo)
        ventanaActualizarNombre.title("Ingresa el nuevo apellido a registrar.")
        ventanaActualizarNombre.geometry("400x150")
        ventanaActualizarNombre.config(bg="lightblue")
        cajaTexto = tk.Entry(ventanaActualizarNombre)
        cajaTexto.place(x=100, y=50)
        if pos == 1:
            botonAceptar = tk.Button(ventanaActualizarNombre, text="Actualizar",font=("Verdana", 10),bg="green",command=lambda:actualizarInfo(ventanaActualizarNombre,cajaTexto,1),fg="white")
            botonAceptar.place(x=150, y=100)
        else:
            botonAceptar = tk.Button(ventanaActualizarNombre, text="Actualizar",font=("Verdana", 10),bg="green",command=lambda:actualizarInfo(ventanaActualizarNombre,cajaTexto,2),fg="white")
            botonAceptar.place(x=150, y=100)
    def opcionActualizarNombre():
        ventanaActualizarNombre=tk.Toplevel(ventanaActualizarInfo)
        ventanaActualizarNombre.title("Ingresa el nuevo nombre a registrar.")
        ventanaActualizarNombre.geometry("400x150")
        ventanaActualizarNombre.config(bg="lightblue")
        cajaTexto = tk.Entry(ventanaActualizarNombre)
        cajaTexto.place(x=100, y=50)
        
        botonAceptar = tk.Button(ventanaActualizarNombre, text="Actualizar",font=("Verdana", 10),bg="green",command=lambda:actualizarInfo(ventanaActualizarNombre,cajaTexto,0),fg="white")
        botonAceptar.place(x=150, y=100)

    def mostrarInfoMentor(carnet):
        for sede in diccMentores.keys():
                for mentor in diccMentores.get(sede, []):
                    if mentor[0] == carnet:
                        nombre = mentor[1][0]
                        primerApellido = mentor[1][1]
                        segundoApellido = mentor[1][2]
                        correo = mentor[3]
                        tipo= "Estudiante mentor"
                        break
        labelNombre = tk.Label(ventanaActualizarInfo, text=f"Nombre: {nombre}")
        labelNombre.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelNombre.place(x=75, y=50)
        labelPrimerApellido = tk.Label(ventanaActualizarInfo, text=f"Primer apellido: {primerApellido}")
        labelPrimerApellido.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelPrimerApellido.place(x=75, y=80)
        labelSegundoApellido = tk.Label(ventanaActualizarInfo, text=f"Segundo apellido: {segundoApellido}")
        labelSegundoApellido.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelSegundoApellido.place(x=75, y=110)
        labelCorreo = tk.Label(ventanaActualizarInfo, text=f"Correo: {correo}")
        labelCorreo.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelCorreo.place(x=75, y=170)
        labelTipo = tk.Label(ventanaActualizarInfo, text=f"Tipo: {tipo}")
        labelTipo.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelTipo.place(x=75, y=200)

    def mostrarInfoEstudiante(carnet):
        
        informacion = diccEstudiantes.get(carnet, [])
        nombre = informacion[0][0]
        primerApellido = informacion[0][1]
        segundoApellido = informacion[0][2]
        telefono = informacion[1]
        correo = informacion[2]
        tipo= "Primer ingreso"
  
        labelNombre = tk.Label(ventanaActualizarInfo, text=f"Nombre: {nombre}")
        labelNombre.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelNombre.place(x=75, y=50)
        labelPrimerApellido = tk.Label(ventanaActualizarInfo, text=f"Primer apellido: {primerApellido}")
        labelPrimerApellido.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelPrimerApellido.place(x=75, y=80)
        labelSegundoApellido = tk.Label(ventanaActualizarInfo, text=f"Segundo apellido: {segundoApellido}")
        labelSegundoApellido.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelSegundoApellido.place(x=75, y=110)
        labelTelefono = tk.Label(ventanaActualizarInfo, text=f"Teléfono: {telefono}")
        labelTelefono.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelTelefono.place(x=75, y=140)
        labelCorreo = tk.Label(ventanaActualizarInfo, text=f"Correo: {correo}")
        labelCorreo.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelCorreo.place(x=75, y=170)
        labelTipo = tk.Label(ventanaActualizarInfo, text=f"Tipo: {tipo}")
        labelTipo.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelTipo.place(x=75, y=200)

        
    def obtenerCarnet(buscarEstudiantetxt,cajaTexto):
        global carnet
        carnet=cajaTexto.get()
        if len(carnet)==10:
            if carnet in totalCarnets:
                if carnet[:4]=="2024":
                    mostrarInfoEstudiante(carnet)
                else:
                    mostrarInfoMentor(carnet)
                buscarEstudiantetxt.destroy()
                habilitarOpciones()
                return carnet
            else:
                messagebox.showerror("Error", "El carnet ingresado no se encuentra registrado.")
                cajaTexto.delete(0,END)
        else:
            messagebox.showerror("Error", "El formato del carnet es incorrecto. Debes al menos 10 valores numéricos.")
            cajaTexto.delete(0,END)

    def buscarEstudiante():
        buscarEstudiantetxt=tk.Toplevel(ventanaActualizarInfo)
        buscarEstudiantetxt.title("Ingrese el número de carnet del estudiante a buscar.")
        buscarEstudiantetxt.geometry("400x150")
        buscarEstudiantetxt.config(bg="lightblue")
        cajaTexto = tk.Entry(buscarEstudiantetxt)
        cajaTexto.place(x=100, y=50)
        
        botonAceptar = tk.Button(buscarEstudiantetxt, text="Agregar",font=("Verdana", 10),bg="green",command=lambda:obtenerCarnet(buscarEstudiantetxt,cajaTexto),fg="white")
        botonAceptar.place(x=150, y=100)

    def cerrarVentanaActualizarInfo():
        ventanaActualizarInfo.destroy()
        ventana.deiconify()
    


    ventanaActualizarInfo = tk.Toplevel(ventana)
    ventanaActualizarInfo.title("Ventana de actualización de información.")
    ventanaActualizarInfo.geometry("550x300")
    ventanaActualizarInfo.config(bg="lightblue")
    ventana.withdraw()

    #Texto en la ventana
    label = tk.Label(ventanaActualizarInfo, text="Ventana para actualizar información de los estudiantes.")
    label.config(fg="green", bg="lightgrey", font=("Verdana", 12))
    label.place(x=25, y=10)

    #Botones
    botonVolver = tk.Button(ventanaActualizarInfo, text="Volver",font=("Verdana", 10),bg="red",command=cerrarVentanaActualizarInfo,fg="white")
    botonVolver.place(x=490, y=265)

    #Menu desplegable
    menu = tk.Menu(ventanaActualizarInfo)
    opciones = tk.Menu(menu,tearoff=0)
    opciones.add_command(label="Buscar estudiante",command=buscarEstudiante)
    opciones.add_command(label="Actualizar nombre",command=opcionActualizarNombre,state=DISABLED)
    opciones.add_command(label="Actualizar primer apellido",command=lambda:opcionActualizarApellido(1),state=DISABLED)
    opciones.add_command(label="Actualizar segundo apellido",command=lambda:opcionActualizarApellido(2),state=DISABLED)
    opciones.add_command(label="Actualizar teléfono",command=opcionActualizarTelefono,state=DISABLED)
    opciones.add_command(label="Actualizar correo",command=opcionActualizarCorreo,state=DISABLED)


    menu.add_cascade(label="Opciones para actualiar información", menu=opciones)
    ventanaActualizarInfo.config(menu=menu)
    

def opcionAsignarMentores():
    global diccEstudiantes
    global diccMentores
    diccEstudiantes=asignarMentores(diccEstudiantes,diccMentores,estructuraCarrerasCantidad)
    return diccEstudiantes


def crearMentores():
    
    def mostrarInfo():
        for i in range(1, 6):
            for j in range(1, 2):
                matrizLabel[i][j].destroy()
                
        sedes = diccMentores.keys()
        
        for i, sede in enumerate(sedes, start=1):
            for j in range(1, 2):
                contenido = "\n".join([f"{sede[0]}: {sede[1:]}" for sede in diccMentores.get(sede, [])])

                text = tk.Text(ventanaMentores, width=130 if j == 1 else 10, height=4, relief="solid")
                text.grid(column=j, row=i)
                text.place(x=51 + (j * 75), y=46 + (i * 70))
                text.insert("1.0", contenido)
                text.tag_configure("center", justify="center")
                text.tag_add("center", "1.0", "end")
                text.config(state="disabled")
                matrizLabel[i][j] = text
    
    def cerrarVentanaMentores():
        ventanaMentores.destroy()
        ventana.deiconify()

    ventanaMentores = tk.Toplevel(ventana)
    ventanaMentores.title("Pestaña de los mentores")
    ventanaMentores.geometry("1185x525")
    ventanaMentores.config(bg="lightblue")
    ventana.withdraw()

    #Texto en la ventana
    label = tk.Label(ventanaMentores, text="Pestaña de los mentores")
    label.config(fg="green", bg="lightgrey", font=("Verdana", 12))
    label.place(x=25, y=10)

    #Botones
    botonVolver = tk.Button(ventanaMentores, text="Volver",font=("Verdana", 10),bg="red",command=cerrarVentanaMentores,fg="white")
    botonVolver.place(x=1110, y=485)

    matrizLabel = [[None for _ in range(2)] for _ in range(6)]

    global diccMentores

    diccMentores={}
    diccMentores=generarCarnetsMentores(estructuraCarrerasCantidad,codigosSedes,totalCarnets,totalNumeros,totalCorreos,diccMentores)
    
    diccionarioVacio={(0,0):"Sede", (0,1):"Información de mentores", (1,0):"CTLSC", (2,0):"CTLSJ", (3,0):"CAL", (4,0):"CTCC", (5,0):"CAA"}
    
    for i in range(6):       
        for j in range(2):
            info=diccionarioVacio.get((i,j),"")
            label = tk.Label(ventanaMentores,width=148 if j == 1 else 10,height=4,relief="solid",anchor=CENTER)
            label.grid(column=j, row=i)
            label.place(x=50+(j*75), y=45+(i*69))
            matrizLabel[i][j]=label
            matrizLabel[i][j].config(text=info)

    mostrarInfo()
  

def estudiantesCarreraPorSede(totalCarnets):
    global diccEstudiantes
    diccEstudiantes={}
    diccEstudiantes=generarCarnetsEstudiantes(totalAdmitidos, estructuraCarrerasCantidad,codigosSedes,totalCarnets,totalNumeros,totalCorreos,diccEstudiantes)
    messagebox.showinfo("Información","Se han insertado satisfactoriamente la información de cada estudiantes admitido")
    return diccEstudiantes


def crearEstructuraEstudiantesCarreraSede():
    info=obtenerSedesCarreras()
    estructuraAdmitidosCarrera={}
    for sede in info.keys():
        listaAdmitidosCarrera=[]
        for carrera in info[sede]:
            listaAdmitidosCarrera.append([carrera,0])
        estructuraAdmitidosCarrera[sede]=listaAdmitidosCarrera
    
    return estructuraAdmitidosCarrera

def estudiantesPorSede():
    
    def distribuirAdmitidos(totalAdmitidos, estructuraCarrerasCantidad):
        for sede, carreras in estructuraCarrerasCantidad.items():
            total_cupos = totalAdmitidos[sede]

            for carrera in carreras[:-1]:
                cupos = total_cupos // random.randint(4, 9)
                carrera[1] = cupos
                total_cupos -= cupos

            carrera = carreras[-1]
            carrera[1] = total_cupos

        return estructuraCarrerasCantidad

    def actualizarMatriz():
        for i in range(1, 6):
            for j in range(1, 3):
                matrizLabel[i][j].destroy()
                
        sedes = totalAdmitidos.keys()
        
        for i, sede in enumerate(sedes, start=1):
            for j in range(1, 3):
                if j == 1:
                    contenido = totalAdmitidos.get(sede, "")
                else:
                    contenido = "\n".join([f"{carrera[0]}: {carrera[1]}" for carrera in estructuraCarrerasCantidad.get(sede, [])])

                text = tk.Text(ventanaEstudiantesSede, width=72 if j == 2 else 10, height=4, relief="solid")
                text.grid(column=j, row=i)
                text.place(x=30 + (j * 75), y=40 + (i * 70))
                text.insert("1.0", contenido)
                text.tag_configure("center", justify="center")
                text.tag_add("center", "1.0", "end")
                text.config(state="disabled")
                matrizLabel[i][j] = text

   
    def verificarAdmitidos():
        for sede in totalAdmitidos.keys():
            if totalAdmitidos[sede]==0:
                return False
        return True

    def recolectarInfo(sede,cajaTexto,menuAdmitidos):
        cantidad=cajaTexto.get()
        if cantidad.isdigit():
            totalAdmitidos[sede]=int(cantidad)
            distribuirAdmitidos(totalAdmitidos,estructuraCarrerasCantidad)
            menuAdmitidos.destroy()
        else:
            messagebox.showerror("Error", "Debe ingresar valores númericos enteros unicamente")
            cajaTexto.delete(0,END)
    
    def menuAdmitidos(sede):
        menuAdmitidos=tk.Toplevel(ventanaEstudiantesSede)
        menuAdmitidos.title("Ingrese cantidad de estudiantes admitidos")
        menuAdmitidos.geometry("400x150")
        menuAdmitidos.config(bg="lightblue")
        cajaTexto = tk.Entry(menuAdmitidos)
        cajaTexto.place(x=100, y=50)
        
        botonAceptar = tk.Button(menuAdmitidos, text="Agregar",font=("Verdana", 10),bg="green",command=lambda:recolectarInfo(sede,cajaTexto,menuAdmitidos),fg="white")
        botonAceptar.place(x=150, y=100)
        
        

    def mostrarMatrizVacia():

        diccionarioVacio={(0,0):"Sede", (0,1):"Admitidos",(0,2):"Cantidad de estudiantes por carrera", (1,0):"CTLSC", (2,0):"CTLSJ", (3,0):"CAL", (4,0):"CTCC", (5,0):"CAA"}
        for i in range(6):       
            for j in range(3):
                info=diccionarioVacio.get((i,j),"")
                label = tk.Label(ventanaEstudiantesSede,width=82 if j==2 else 10,height=4,relief="solid",anchor=CENTER)
                label.grid(column=j, row=i)
                label.place(x=30+(j*75), y=45+(i*69))
                matrizLabel[i][j]=label
                matrizLabel[i][j].config(text=info)
          
    def cerrarVentana():
        if verificarAdmitidos():
            ventanaEstudiantesSede.destroy()
            habilitarOpciones()
            ventana.deiconify()
        else:
            messagebox.showerror("Error", "Debe ingresar al menos una cantidad de estudiantes admitidos por sede")

    #Configuración de la ventana
    ventana.withdraw()
    ventanaEstudiantesSede=tk.Toplevel(ventana)
    ventanaEstudiantesSede.title("Estudiantes por sede")
    ventanaEstudiantesSede.geometry("825x525")
    ventanaEstudiantesSede.config(bg="lightblue") 

    #Texto en la ventana
    label = tk.Label(ventanaEstudiantesSede, text="Estudiantes por sede")
    label.config(fg="green", bg="lightgrey", font=("Verdana", 12))
    label.place(x=25, y=10)

    #Botones
    botonVolver = tk.Button(ventanaEstudiantesSede, text="Volver",font=("Verdana", 10),bg="red",command=cerrarVentana,fg="white")
    botonVolver.place(x=750, y=485)

    #Menu desplegable
    menu = tk.Menu(ventanaEstudiantesSede)
    opciones = tk.Menu(menu,tearoff=0)
    opciones.add_command(label="Sede San Carlos", command=lambda:menuAdmitidos("CTLSC"))
    opciones.add_command(label="Sede San José", command=lambda:menuAdmitidos("CTLSJ"))
    opciones.add_command(label="Sede Limón", command=lambda:menuAdmitidos("CAL"))
    opciones.add_command(label="Sede Cartago", command=lambda:menuAdmitidos("CTCC"))
    opciones.add_command(label="Sede Alajuela", command=lambda:menuAdmitidos("CAA"))
    opciones.add_command(label="Actualizar matriz", command=actualizarMatriz)


    menu.add_cascade(label="Ingresar estudiantes admitidos", menu=opciones)
    ventanaEstudiantesSede.config(menu=menu)
    
    #MatrizVacia
    matrizLabel = [[None for _ in range(3)] for _ in range(6)]
    
    mostrarMatrizVacia()
    

def habilitarOpciones():
    boton2.config(state=tk.NORMAL)
    boton3.config(state=tk.NORMAL)
    boton4.config(state=tk.NORMAL)
    boton5.config(state=tk.NORMAL)
    boton6.config(state=tk.NORMAL)
    boton7.config(state=tk.NORMAL)
    boton8.config(state=tk.NORMAL)

#Personalización de la ventana
ventana.title("Atención a la generación de 2024.")
ventana.geometry("550x300")
#ventana.iconbitmap("logo.ico") para cambiar el icono de la aplicación
ventana.config(bg="lightblue")

#Texto en la ventana
label = tk.Label(ventana, text="Bienvenid@ a la aplicación de atención a la generación 2024.")
label.config(fg="green", bg="lightgrey", font=("Verdana", 12))
label.place(x=25, y=10)

#Creacion botones
boton1 = tk.Button(ventana, text="Estudiantes por sede",font=("Verdana", 10),command=estudiantesPorSede)
boton2 = tk.Button(ventana, text="Estudiantes de carrera por sede",font=("Verdana", 10),state="disabled",command=lambda:estudiantesCarreraPorSede(totalCarnets))
boton3 = tk.Button(ventana, text="Crear mentores",font=("Verdana", 10),state="disabled",command=crearMentores)
boton4 = tk.Button(ventana, text="Asignar mentores",font=("Verdana", 10),state="disabled",command=opcionAsignarMentores)
boton5 = tk.Button(ventana, text="Actualizar estudiante",font=("Verdana", 10),command=opcionActualizarEstudiante)
boton6 = tk.Button(ventana, text="Generar reportes",font=("Verdana", 10),state="disabled")
boton7 = tk.Button(ventana, text="Crear base de datos en Excel",font=("Verdana", 10),state="disabled")
boton8 = tk.Button(ventana, text="Enviar correo",font=("Verdana", 10),state="disabled")
boton9 = tk.Button(ventana, text="Salir",font=("Verdana", 10),bg="red",command=ventana.destroy,fg="white")


#Posicionamiento de los botones
boton1.place(x=85, y=50)
boton2.place(x=45, y=95)
boton3.place(x=90, y=140)
boton4.place(x=85, y=185)
boton5.place(x=325, y=50)
boton6.place(x=335, y=95)
boton7.place(x=305, y=140)
boton8.place(x=335, y=185)
boton9.place(x=475, y=260)

#Creación de la estructura de datos
#estructuraCarrerasCantidad=crearEstructuraEstudiantesCarreraSede()


ventana.mainloop()


