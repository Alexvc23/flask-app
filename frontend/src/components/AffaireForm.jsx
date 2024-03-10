// import React, { useEffect, useState } from 'react';

// const apiAddress = "http://localhost:5000";


// const initialLocation = { department: '', commune: '', precision: '' };

// const AffaireForm = () => {

//     const [locations, setLocations] = useState([initialLocation]);
//     const [isMultipleMode, setIsMultipleMode] = useState(false);

//     const [nomDeLaffaire, setNomDeLaffaire] = useState(''); // title for the case (string)

//     const [department, setDepartment] = useState(''); // variable to store only the department choosen by the client  (string)
//     const [departments, setDepartments] = useState([]); // variable to store the entire department list fetch from the backend !array[]

//     const [commune, setCommune] = useState(''); // variable to store only the commune chosses by the client (string)
//     const [communes, setCommunes] = useState([]); // variable to store the entire commune list fetched form the backed 

//     const [precision, setPrecision] = useState(''); // case description

//     /*
    
//                  #       ####   ####    ##   #         ###### #    # #    #  ####  ##### #  ####  #    #  ####
//                  #      #    # #    #  #  #  #         #      #    # ##   # #    #   #   # #    # ##   # #
//                  #      #    # #      #    # #         #####  #    # # #  # #        #   # #    # # #  #  ####
//                  #      #    # #      ###### #         #      #    # #  # # #        #   # #    # #  # #      #
//                  #      #    # #    # #    # #         #      #    # #   ## #    #   #   # #    # #   ## #    #
//                  ######  ####   ####  #    # ######    #       ####  #    #  ####    #   #  ####  #    #  ####
    
//     */

//     const fetchDepartments = async () => {
//         fetch(`${apiAddress}/departement`)
//             .then(response => response.json())
//             .then(data => {setDepartments(data); console.log(departments)}) // here we assign all the departments inside the useState variable departments
//             .catch(error => console.error('Error fetching departements:', error));
//     }
//     // ─────────────────────────────────────────────────────────────────────
    
//     const fetchCommunes = async () => {
//         if (department) {
//             fetch(`${apiAddress}/communes?dep_code=${department}`)
//                 .then(response => response.json())
//                 .then(data => { setCommunes(data); console.log(communes[3]) })
//                 .catch(error => console.error('Error fetching departements:', error));
//         }
//     };
//     // ─────────────────────────────────────────────────────────────────────

//     const toggleMode = (event) => {
//         event.preventDefault();
//         setIsMultipleMode(!isMultipleMode);
//     };

//     // ─────────────────────────────────────────────────────────────────────
//     const updateLocationChangeJSX = (index, field, value) => {
//         const newLocations = [...locations];
//         newLocations[index][field] = value;
//         setLocations(newLocations);
//     };

//     /*
    
//                     #    #  ####  ######    ###### ###### ###### ######  ####  #####  ####
//                     #    # #      #         #      #      #      #      #    #   #   #
//                     #    #  ####  #####     #####  #####  #####  #####  #        #    ####
//                     #    #      # #         #      #      #      #      #        #        #
//                     #    # #    # #         #      #      #      #      #    #   #   #    #
//                      ####   ####  ######    ###### #      #      ######  ####    #    ####
    
//     */
// useEffect(() => {
//         fetchDepartments();
//     }, []); // Empty dependency array means this effect runs once on mount

//     // ─────────────────────────────────────────────────────────────────────
//     useEffect(() => {
//         fetchCommunes();
//     }, [department]);
//     // ─────────────────────────────────────────────────────────────────────

//     // useEffect(() => {
//     //     ini
//     // }, [commune])



//     /*

//         #  ####  #    #
//         # #       #  #
//         #  ####    ##
//         #      #   ##
//     #    # #    #  #  #
//     ####   ####  #    #

//     */
//     return (
//         //  Center align items horizontally and vertically, minimum height of screen, and light gray background
//         <div className="flex justify-center items-center min-h-screen bg-gray-100">
//             {/* Width full under small screen, max-width large under large screen, white background, shadow around form, rounded corners, padding, and margin bottom */}
//             <form className="w-full max-w-lg bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">

//                 <div >
//                     < button onClick={toggleMode} className={`${isMultipleMode ? 'bg-blue-500 mb-5 hover:bg-blue-700' : 'bg-green-500 mb-5 hover:bg-green-700'}
//                     text-white font-bold py-2 px-4 rounded transition duration-300 ease-in-out transform hover:-translate-y-1 
//                     hover:scale-110`}>
//                         Switch to {isMultipleMode ? 'Single' : 'Multiple'} Mode
//                     </button>
//                 </div>

//                 {/* Margin bottom */}
//                 <div className="mb-4">
//                     {/* Block display, dark gray text, small text size, bold font, margin bottom */}
//                     <label htmlFor="nomDeLaffaire" className="block text-gray-700 text-sm font-bold mb-2">
//                         Nom de l'Affaire <span className="text-red-500"> * </span>
//                     </label>

//                     {/* Full width, padding, round border, shadow, dark gray text, leading tight, focus outline none, focus shadow outline */}
//                     <input type="text" id="nomDeLaffaire" value={nomDeLaffaire}
//                         onChange={(e) => setNomDeLaffaire(e.target.value)}
//                         className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
//                 </div>

//             {/* // ───────────────────────────────────────────────────────────────────────────── */}

//                 {/* Similar structure repeated for other form fields... */}
//                 <div className="mb-4">
//                     <label htmlFor="department" className="block text-gray-700 text-sm font-bold mb-2">
//                         Département
//                     </label>
//                     <select id="department" value={department}
//                         onChange={(e) => setDepartment(e.target.value)} // here we assign the department choosen by the user, that eventually it will be used to search the commune
//                         className="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
//                         <option value="">Choisissez un département</option> {/*  the option html element allow us to set each individual item in the selection list */}
//                         {departments.map((dep) => (
//                             <option key={dep.DEP_CODE} value={dep.DEP_CODE}>{`${dep.DEP_NOM} (${dep.DEP_CODE})`}</option> /* in the deparments useState variable array we have all departments, 
//                                                                                                                              we will put them in the list programically with the map method  */
//                         ))}
//                     </select>
//                 </div>

//             {/* // ───────────────────────────────────────────────────────────────────────────── */}

//                 <div className="mb-4">
//                     <label htmlFor="commune" className="block text-gray-700 text-sm font-bold mb-2">
//                         Commune
//                     </label>
//                     <select id="commune" value={commune}
//                         onChange={(e) => setCommune(e.target.value)}
//                         className="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
//                         <option value="">Select a commune</option>
//                         {communes.map((com) => (
//                             <option key={com.COM_CODE} value={com.COM_NOM}>{`${com.COM_NOM} (${com.COM_CODE})`}</option>
//                         ))}
//                     </select>
//                 </div>

//             {/* // ───────────────────────────────────────────────────────────────────────────── */}

//                 <div className="mb-6">
//                     <label htmlFor="precision" className="block text-gray-700 text-sm font-bold mb-2">
//                         Précision <span className="text-red-500"> * </span>
//                     </label>
//                     <input type="text" id="precision" value={precision}
//                         onChange={(e) => setPrecision(e.target.value)}
//                         className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" />
//                 </div>

//             {/* // ───────────────────────────────────────────────────────────────────────────── */}

//                 {/* Button with background color blue, on hover darker blue, white text, bold, padding, rounded corners, focus outline none, focus shadow outline */}
//                 <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded 
//                 focus:outline-none focus:shadow-outline transition duration-300 ease-in-out transform 
//                 hover:-translate-y-1 hover:scale-110 ">
//                     Submit
//                 </button>
//             </form>
//         </div>
//     );
// }

// export default AffaireForm;

import React, { useEffect, useState } from 'react';

const apiAddress = "http://localhost:5000";

const initialLocation = { department: '', commune: '', precision: '' };
const initialCommunesByIndex = {communeList: [] };

const AffaireForm = () => {
    const [locations, setLocations] = useState([initialLocation]);
    const [isMultipleMode, setIsMultipleMode] = useState(false);
    const [nomDeLaffaire, setNomDeLaffaire] = useState('');
    const [departments, setDepartments] = useState([]);
    const [department, setDepartment] = useState(''); // variable to store only the department choosen by the client  (string)
    const [communes, setCommunes] = useState([]);
    const [communesByIndex, setCommunesByIndex] = useState([initialCommunesByIndex]);

    // ─────────────────────────────────────────────────────────────────────

    const fetchDepartments = async () => {
        await fetch(`${apiAddress}/departement`)
            .then(response => response.json())
            .then(data => setDepartments(data))
            .catch(error => console.error('Error fetching departments:', error));
    };

    const fetchCommunes = async () => {
        if (department) {
            await fetch(`${apiAddress}/communes?dep_code=${department}`)
                .then(response => response.json())
                .then(data => setCommunes(data))
                .catch(error => console.error('Error fetching departements:', error));
        }
    };

    const updateCommunesInLocations = async () => {
        fetchCommunes();
    }

    const updateCommuneByIndex = (index, arrayCommunes) => {
        // Make a copy of the communesByIndex array to avoid mutating the original state directly.
        const updatedCommunesByIndex = [...communesByIndex];

        // Update the communeList property of the object at the specified index.
        updatedCommunesByIndex[index] = { ...updatedCommunesByIndex[index], communeList: arrayCommunes };

        // Update the state with the modified array.
        setCommunesByIndex(updatedCommunesByIndex);
    };


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

    const addLocation = () => {
        setLocations([...locations, initialLocation]);
    };

    const toggleMode = (event) => {
        event.preventDefault();
        setIsMultipleMode(!isMultipleMode);
    };

    const removeLocation = (index) => {
        const filteredLocations = locations.filter((_, idx) => idx !== index);
        setLocations(filteredLocations);
    };

    // ─────────────────────────────────────────────────────────────────────────────

    // fetchs the department at the component mount life cycle
    useEffect(() => {
        fetchDepartments();
    }, []);

    // every time the user in the JSX chooses a department and updates the department State variable this useEffect is called
    useEffect(() => {
        fetchCommunes();
    }, [department]);

    //ever time communes state variable is update this ufeEffect funtion in called
    useEffect(() => {
        console.log(`number of comunes ${communes.length} in department ${department}`);
    }, [communes])

    useEffect(() => {
        if (communesByIndex.some)
        {
            console.log(`number of elements in communesByIndex:${communesByIndex.length}`);
            for (let i = 0; i < communesByIndex.length; i++)
                console.log(`communesByIndex { index: ${i} COMMUNE LIST: ${communesByIndex[i].communeList}}`);
        }

    }, [communesByIndex])


    // ─────────────────────────────────────────────────────────────────────────────

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