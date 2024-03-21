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

    // Function: addLocation
    // Description: This function adds a new location to the list of locations.
    // It updates the state variable 'locations' by appending the 'initialLocation' to it.
    const addLocation = () => {
        setLocations([...locations, initialLocation]); // Spread operator is used to create a new array with the existing locations and the new initialLocation.
    };

    // ─────────────────────────────────────────────────────────────────────

    // Function: toggleMode
    // Description: This function toggles the mode between single and multiple modes.
    // It takes an event object as a parameter and prevents its default behavior.
    // Then, it toggles the value of 'isMultipleMode', which determines whether the app is in multiple mode or not.
    const toggleMode = (event) => {
        event.preventDefault(); // Prevents the default behavior of the event, such as form submission.
        setIsMultipleMode(!isMultipleMode); // Toggles the value of 'isMultipleMode' using the logical NOT operator.
    };

    // ─────────────────────────────────────────────────────────────────────

    // Function: removeLocation
    // Description: This function removes a location from the list of locations based on the provided index.
    // It filters out the location at the given index from the 'locations' array and updates the state variable 'locations' with the filtered array.
    const removeLocation = (index) => {
        // 'filter' is a higher-order function available in JavaScript arrays.
        // It creates a new array with all elements that pass the test implemented by the provided callback function.
        // In this case, it's filtering out the location at the given 'index'.
        // Parameters:
        // - '_' (underscore): Represents the current value being processed in the array. Since we're not using it here, we're using '_' as a convention to indicate it's unused.
        // - 'idx': Represents the index of the current element being processed in the array.
        const filteredLocations = locations.filter((_, idx) => idx !== index);

        // After filtering out the location at the given 'index', 'filteredLocations' contains all locations except the one to be removed.

        // Finally, we update the 'locations' state variable with the filtered array, effectively removing the location at the specified 'index'.
        setLocations(filteredLocations); // Updates the 'locations' state variable with the filtered array.
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
        fetch(`${apiAddress}/departement`)
            .then(response => response.json())
            .then(data => {
                if (Array.isArray(data)) { // Check if data is an array
                    setDepartments(data);
                } else {
                    console.error('Fetched data is not an array:', data);
                    setDepartments([]); // Reset to default empty array if not an array
                }
            })
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

    // ─────────────────────────────────────────────────────────────────────

    const handleSubmit = async (event) => {
        event.preventDefault();


        // ─────────────────────────────────────────────────────────────

        // Construct the payload from the state
        // Description: This code constructs a payload object using data from the application state.
        // The payload is structured to contain information about a specific affair and its associated locations.
        // example

        /*             Payload:
                    {
                        nomDeLaffaire: "Affair Name",
                        locations: [
                            {
                                department: "Department 1",
                                commune: "Commune 1",
                                precision: "Precision 1"
                            },
                            {
                                department: "Department 2",
                                commune: "Commune 2",
                                precision: "Precision 2"
                            },

                             Additional locations can be added as needed
                        ]
                    } */

        const payload = {
            // 'nomDeLaffaire' represents the name/title of the affair. It is taken from the 'nomDeLaffaire' state variable.
            nomDeLaffaire: nomDeLaffaire,

            // 'locations' contains an array of objects representing the locations associated with the affair.
            // Each object in the 'locations' array contains information about a specific location, such as department, commune, and precision.
            // The array is constructed by mapping over the 'locations' state variable.

            locations: locations.map(({ department, commune, precision }) => ({
                department,
                commune,
                precision
            }))
        };
        // ─────────────────────────────────────────────────────────────

        // Send a Post request to the backend
        try {
            // Send a POST request to the server with payload data
            // Description: This code sends a POST request to a specified API endpoint with a payload containing data from the application state.
            // It uses the Fetch API to make an asynchronous HTTP request.
            const response = await fetch(`${apiAddress}/my-endpoint`, {
                method: 'POST', // Specifies the HTTP method as POST
                headers: {
                    'content-Type': 'application/json', // Sets the Content-Type header to indicate that the request body is JSON
                },
                body: JSON.stringify(payload), // Converts the payload object to a JSON string and includes it in the request body
            });

            // Check if the response from the server is successful (status code 2xx)
            if (!response.ok) {
                throw new Error('Network response was not ok'); // Throws an error if the response status is not ok
            }

            // If the response is successful, parse the JSON data returned by the server
            const data = await response.json(); // Parses the JSON response body asynchronously
            console.log('Success: ', data); // Logs the parsed data to the console, assuming the server responds with JSON

            // Now clear the form and provide some input to the user
            // Description: This section of code executes after a successful response from the server.
            // It may include logic to clear the form fields and provide feedback to the user indicating that the request was successful.
            // Specific implementation details for clearing the form and providing user input are not included in this snippet.

        }
        catch (error) {
            console.error('Error: ', error);
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
                                {index !== 0 && (<button type="button" onClick={() => removeLocation(index)} className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
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

                <button type="submit" onClick={handleSubmit}className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-110">
                    Submit
                </button>
            </form>
        </div>
    );
}

export default AffaireForm;