import React, { useEffect, useState } from 'react';

const apiAddress = "http://localhost:5000";

const initialLocation = { department: '', commune: '', precision: '' };
const initialCommunesByIndex = { communeList: [] };

const AffaireForm = () => {
    const [locations, setLocations] = useState([initialLocation]);
    const [isMultipleMode, setIsMultipleMode] = useState(false);
    const [nomDeLaffaire, setNomDeLaffaire] = useState('');
    const [departments, setDepartments] = useState([]);
    const [department, setDepartment] = useState(''); // variable to store only the department choosen by the client  (string)
    const [communes, setCommunes] = useState([]);
    const [communesByIndex, setCommunesByIndex] = useState([initialCommunesByIndex]);

    // ─────────────────────────────────────────────────────────────────────

    /*

      ,,                               ,,          ,...                                      ,,
    `7MM                             `7MM        .d' ""                               mm     db
      MM                               MM        dM`                                  MM
      MM  ,pW"Wq.   ,p6"bo   ,6"Yb.    MM       mMMmm`7MM  `7MM  `7MMpMMMb.  ,p6"bo mmMMmm `7MM  ,pW"Wq.`7MMpMMMb.  ,pP"Ybd
      MM 6W'   `Wb 6M'  OO  8)   MM    MM        MM    MM    MM    MM    MM 6M'  OO   MM     MM 6W'   `Wb MM    MM  8I   `"
      MM 8M     M8 8M        ,pm9MM    MM        MM    MM    MM    MM    MM 8M        MM     MM 8M     M8 MM    MM  `YMMMa.
      MM YA.   ,A9 YM.    , 8M   MM    MM        MM    MM    MM    MM    MM YM.    ,  MM     MM YA.   ,A9 MM    MM  L.   I8
    .JMML.`Ybmd9'   YMbmd'  `Moo9^Yo..JMML.    .JMML.  `Mbod"YML..JMML  JMML.YMbmd'   `Mbmo.JMML.`Ybmd9'.JMML  JMML.M9mmmP'

    */
    const updateCommuneByIndex = (index, arrayCommunes) => {
        const updatedCommunesByIndex = [...communesByIndex];
        // Ensure arrayCommunes is always an array to avoid runtime errors.
        updatedCommunesByIndex[index] = {
            ...updatedCommunesByIndex[index],
            communeList: Array.isArray(arrayCommunes) ? arrayCommunes : [],
        };
        // console.log('Updating communesByIndex with:', arrayCommunes);
        setCommunesByIndex(updatedCommunesByIndex);
    };

    // ─────────────────────────────────────────────────────────────────────

    /*  As our original data structure that holds all the colcations chosen by the client are like this:
        [{ department: '', commune: '', precision: '' }][..]
        the updateLocationChangeJSX function allow us to update each attibute individually, for instacen COMUNE or DEMARPTMENT */
    const updateLocationChangeJSX = (index, field, value) => {

        // Create a copy of the 'locations' array to avoid mutating the original state directly.
        const updatedLocations = [...locations];

        // Update the specified location object within the copied array, first copy all the attibutes from the selected INDEX
        // then modifies the specified field and assigs a value
        updatedLocations[index] = { ...updatedLocations[index], [field]: value };

        // Set the state with the updated array of locations.
        setLocations(updatedLocations);
    };
    // ─────────────────────────────────────────────────────────────────────

    const addLocation = () => {
        setLocations([...locations, initialLocation]);
    };

    // ─────────────────────────────────────────────────────────────────────

    const toggleMode = (event) => {
        event.preventDefault();
        setIsMultipleMode(!isMultipleMode);
    };

    // ─────────────────────────────────────────────────────────────────────

    const removeLocation = (index) => {
        const filteredLocations = locations.filter((_, idx) => idx !== index);
        setLocations(filteredLocations);
    };

    /*

                                                          ,,    ,,
          db      `7MM"""Mq.`7MMF'                      `7MM  `7MM
         ;MM:       MM   `MM. MM                          MM    MM
        ,V^MM.      MM   ,M9  MM       ,p6"bo   ,6"Yb.    MM    MM  ,pP"Ybd
       ,M  `MM      MMmmdM9   MM      6M'  OO  8)   MM    MM    MM  8I   `"
       AbmmmqMA     MM        MM      8M        ,pm9MM    MM    MM  `YMMMa.
      A'     VML    MM        MM      YM.    , 8M   MM    MM    MM  L.   I8
    .AMA.   .AMMA..JMML.    .JMML.     YMbmd'  `Moo9^Yo..JMML..JMML.M9mmmP'


    */
    const fetchDepartments = async () => {
        await fetch(`${apiAddress}/departement`)
            .then(response => response.json())
            .then(data => setDepartments(data))
            .catch(error => console.error('Error fetching departments:', error));
    };

    // ─────────────────────────────────────────────────────────────────────

    const updateCommunesInLocations = async () => {
        if (department) {
            const fetchedCommunes = await fetch(`${apiAddress}/communes?dep_code=${department}`)
                .then(response => response.json())
                .catch(error => console.error('Error fetching communes:', error));
            setCommunes(fetchedCommunes);  // This will trigger another useEffect or callback where you can update the communesByIndex.
            // Ensure this runs only when new communes are fetched.
            locations.forEach((location, idx) => {
                if (location.department === department) {
                    updateCommuneByIndex(idx, fetchedCommunes);
                }
            });
        }
    };

    /*

                                                ,...  ,...                                                                             ,,
                                `7MM"""YMM    .d' "".d' ""                mm                                    mm                   `7MM
                                  MM    `7    dM`   dM`                   MM                                    MM                     MM
    `7MM  `7MM  ,pP"Ybd  .gP"Ya   MM   d     mMMmm mMMmm.gP"Ya   ,p6"bo mmMMmm      ,p6"bo   ,pW"Wq.`7MMpMMMb.mmMMmm `7Mb,od8 ,pW"Wq.  MM  ,pP"Ybd
      MM    MM  8I   `" ,M'   Yb  MMmmMM      MM    MM ,M'   Yb 6M'  OO   MM       6M'  OO  6W'   `Wb MM    MM  MM     MM' "'6W'   `Wb MM  8I   `"
      MM    MM  `YMMMa. 8M""""""  MM   Y  ,   MM    MM 8M"""""" 8M        MM       8M       8M     M8 MM    MM  MM     MM    8M     M8 MM  `YMMMa.
      MM    MM  L.   I8 YM.    ,  MM     ,M   MM    MM YM.    , YM.    ,  MM       YM.    , YA.   ,A9 MM    MM  MM     MM    YA.   ,A9 MM  L.   I8
      `Mbod"YML.M9mmmP'  `Mbmmd'.JMMmmmmMMM .JMML..JMML.`Mbmmd'  YMbmd'   `Mbmo     YMbmd'   `Ybmd9'.JMML  JMML.`Mbmo.JMML.   `Ybmd9'.JMML.M9mmmP'


    */

    // fetchs the department at the component mount life cycle
    useEffect(() => {
        fetchDepartments();
    }, []);

    // ─────────────────────────────────────────────────────────────────────

    useEffect(() => {
        updateCommunesInLocations();
    }, [department]); // Only re-run the effect if department changes.

    // ─────────────────────────────────────────────────────────────────────

    //ever time communes state variable is update this ufeEffect funtion in called
    useEffect(() => {
        console.log(`number of comunes in department ${department}: ${communes.length}`);
    }, [communes])

    /*


       `7MMF'.M"""bgd `YMM'   `MP'
         MM ,MI    "Y   VMb.  ,P
         MM `MMb.        `MM.M'
         MM   `YMMNq.      MMb
         MM .     `MM    ,M'`Mb.
    (O)  MM Mb     dM   ,P   `MM.
     Ymmm9  P"Ybmmd"  .MM:.  .:MMa.


    */

    return (
        <div className="flex justify-center items-center min-h-screen bg-gray-100">
            <form className="w-full max-w-lg bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
                <div >
                    <button onClick={toggleMode} className={`${isMultipleMode ? 'bg-blue-500 mb-5 hover:bg-blue-700' : 'bg-green-500 mb-5 hover:bg-green-700'} text-white font-bold py-2 px-4 rounded transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-110`}>
                        Switch to {isMultipleMode ? 'Single' : 'Multiple'} Mode
                    </button>
                </div>

                <div className="mb-4">
                    <label htmlFor="nomDeLaffaire" className="block text-gray-700 text-sm font-bold mb-2">
                        Nom de l'Affaire <span className="text-red-500"> * </span>
                    </label>
                    <input type="text" id="nomDeLaffaire" value={nomDeLaffaire}
                        onChange={(e) => setNomDeLaffaire(e.target.value)}
                        className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
                </div>

                {/*
                 Iterate over locations to render elements for each location
                 'location' represents the current location object 
                 'index' represents the index of the current location in the array ([i])

                 JSX allows embedding JavaScript expressions
                 Each location in the array corresponds to a JSX element to be rendered

                 Ensure each JSX element rendered inside the map function has a unique 'key' prop

                 The map function returns an array of JSX elements to be rendered by React */}
                {locations.map((location, index) => (
                    <div key={index} className="mb-4">

                        {/* // ───────────────────────────── */}

                        <div className="mb-4">
                            {/* Label for the department select input */}
                            <label htmlFor={`department-${index}`} className="block text-gray-700 text-sm font-bold mb-2">
                                Département
                            </label>
                            {/* Select input for choosing a department */}
                            <select id={`department-${index}`} value={location.department}
                                onChange={(e) => {
                                    const newDepartment = e.target.value;
                                    updateLocationChangeJSX(index, 'department', newDepartment);
                                    setDepartment(newDepartment);
                                }}
                                className="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                                {/* Default option for selecting a department */}
                                <option value="">Choisissez un département</option>
                                {/* Mapping over the departments array to render options */}
                                {departments.map((dep) => (
                                    // Each option corresponds to a department object
                                    <option key={dep.DEP_CODE} value={dep.DEP_CODE}>{dep.DEP_NOM}</option>
                                ))}
                            </select>
                        </div>

                        {/* // ───────────────────────────── */}

                        <div className="mb-4">
                            <label htmlFor={`commune-${index}`} className="block text-gray-700 text-sm font-bold mb-2">
                                Commune
                            </label>
                            <select id={`commune-${index}`} value={location.commune}
                                onChange={(e) => updateLocationChangeJSX(index, 'commune', e.target.value)}
                                className="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                                <option value="">Select a commune</option>
                                {communesByIndex[index]?.communeList.map((com) => (
                                    <option key={com.COM_CODE} value={com.COM_NOM}>{`${com.COM_NOM} (${com.COM_CODE})`}</option>
                                ))}
                            </select>
                        </div>

                        {/* // ───────────────────────────── */}

                        <div className="mb-6">
                            <label htmlFor={`precision-${index}`} className="block text-gray-700 text-sm font-bold mb-2">
                                Précision <span className="text-red-500"> * </span>
                            </label>
                            <input type="text" id={`precision-${index}`} value={location.precision}
                                onChange={(e) => updateLocationChangeJSX(index, 'precision', e.target.value)}
                                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" />
                        </div>

                        {/* // ───────────────────────────── */}

                        {isMultipleMode && (
                            <div className="flex justify-between items-center">
                                {/* remove button */}
                                {/* the elements in the array will be in FILA order (first in last out) */}
                                {/* disable the Remove button for the fist element in the list as we need to have at leat one */}
                                {index != 0 && (<button type="button" onClick={() => removeLocation(index)} className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
                                    Remove Location
                                </button>)}
                                {/* add location button */}
                                {index === locations.length - 1 && (
                                    <button type="button" onClick={addLocation} className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
                                        Add Location
                                    </button>
                                )}
                            </div>
                        )}

                        {/* // ───────────────────────────── */}

                    </div>
                ))}

                <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-110">
                    Submit
                </button>
            </form>
        </div>
    );
}

export default AffaireForm;