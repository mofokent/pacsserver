import os
from pydicom import dcmread

#folder path update

count = 0
dir_path = r'c:\\temp\\'

for path in os.scandir(dir_path):
    if path.is_file():
        count += 1
print('file count:', count)

if count == 0:
    print ('No files to process')

else:
    print('files2process')
    folder_walk = os.walk(dir_path)
    first_file_in_folder = next(folder_walk)[2][0]
    print(first_file_in_folder)

ds = dcmread(dir_path + first_file_in_folder)
#print(ds)
#elem = ds['PatientID']
#PatientID = elem.value
PatientID = ds.data_element('PatientID').value
print (PatientID)
#elem = ds['PatientName']
#PatientName = elem.value

def read_dicom_with_pydicom(dicom_file, dicom_fields):
    """
    Read DICOM file using PyDICOM python library.

    :param dicom_file: DICOM file to read
     :type dicom_file: str
    :param dicom_fields: Dictionary containing DICOM fields and values
     :type dicom_fields: dict

    :return: updated dictionary of DICOM fields and values
     :rtype : dict

    """

    # Read DICOM file
    dicom_dataset = dicom.read_file(dicom_file)

    # Grep information from DICOM header and store them
    # into dicom_fields dictionary under flag Value
    # Dictionnary of DICOM values to be returned
    for name in dicom_fields:
        try:
            description = dicom_fields[name]['Description']
            value = dicom_dataset.data_element(description).value
            dicom_fields[name]['Value'] = value
            print (value)
        except:
            continue

    return dicom_fields

#rename file
#old_name= (dir_path + first_file_in_folder)
#new_name= (dir_path + first_file_in_folder+'.dcm')
#os.rename(old_name, new_name)

#read dicom data, populate db+movefile