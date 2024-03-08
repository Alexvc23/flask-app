import React, { useEffect, useState } from 'react';

const apiAddress = "http://localhost:5000";


const initialLocation = { department: '', commune: '', precision: '' };
const AffaireForm = () => {

    const [location, setLocations] = useState([initialLocation]);
    const [isMultipleMode, setIsMultipleMode] = useState(false);

    const [nomDeLaffaire, setNomDeLaffaire] = useState(''); // title for the case (string)

    const [department, setDepartment] = useState(''); // variable to store only the department choosen by the client  (string)
    const [departments, setDepartments] = useState([]); // variable to store the entire department list fetch from the backend !array[]

    const [commune, setCommune] = useState(''); // variable to store only the commune chosses by the client (string)
    const [communes, setCommunes] = useState([]); // variable to store the entire commune list fetched form the backed 

    const [precision, setPrecision] = useState(''); // case description

    /*
    
                 #       ####   ####    ##   #         ###### #    # #    #  ####  ##### #  ####  #    #  ####
                 #      #    # #    #  #  #  #         #      #    # ##   # #    #   #   # #    # ##   # #
                 #      #    # #      #    # #         #####  #    # # #  # #        #   # #    # # #  #  ####
                 #      #    # #      ###### #         #      #    # #  # # #        #   # #    # #  # #      #
                 #      #    # #    # #    # #         #      #    # #   ## #    #   #   # #    # #   ## #    #
                 ######  ####   ####  #    # ######    #       ####  #    #  ####    #   #  ####  #    #  ####
    
    */

    const fetchDepartments = async () => {
        fetch(`${apiAddress}/departement`)
            .then(response => response.json())
            .then(data => {setDepartments(data); console.log(departments)}) // here we assign all the departments inside the useState variable departments
            .catch(error => console.error('Error fetching departements:', error));
    }
    // ─────────────────────────────────────────────────────────────────────
    
    const fetchCommunes = async () => {
        if (department) {
            fetch(`${apiAddress}/communes?dep_code=${department}`)
                .then(response => response.json())
                .then(data => { setCommunes(data); console.log(communes[3]) })
                .catch(error => console.error('Error fetching departements:', error));
        }
    }
    // ─────────────────────────────────────────────────────────────────────

    const toggleMode = (event) => {
        event.preventDefault();
        setIsMultipleMode(!isMultipleMode);
    }

    // ─────────────────────────────────────────────────────────────────────

    /*
    
                    #    #  ####  ######    ###### ###### ###### ######  ####  #####  ####
                    #    # #      #         #      #      #      #      #    #   #   #
                    #    #  ####  #####     #####  #####  #####  #####  #        #    ####
                    #    #      # #         #      #      #      #      #        #        #
                    #    # #    # #         #      #      #      #      #    #   #   #    #
                     ####   ####  ######    ###### #      #      ######  ####    #    ####
    
    */

    useEffect(() => {
        fetchDepartments();
    }, []); // Empty dependency array means this effect runs once on mount

    // ─────────────────────────────────────────────────────────────────────
    useEffect(() => {
        fetchCommunes();
    }, [department]);
    // ─────────────────────────────────────────────────────────────────────

    // useEffect(() => {
    //     ini
    // }, [commune])



    /*

        #  ####  #    #
        # #       #  #
        #  ####    ##
        #      #   ##
    #    # #    #  #  #
    ####   ####  #    #

    */
    return (
        //  Center align items horizontally and vertically, minimum height of screen, and light gray background
        <div className="flex justify-center items-center min-h-screen bg-gray-100">
            {/* Width full under small screen, max-width large under large screen, white background, shadow around form, rounded corners, padding, and margin bottom */}
            <form className="w-full max-w-lg bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">

                <div >
                    < button onClick={toggleMode} className={`${isMultipleMode ? 'bg-blue-500 mb-5 hover:bg-blue-700' : 'bg-green-500 mb-5 hover:bg-green-700'}
                    text-white font-bold py-2 px-4 rounded transition duration-300 ease-in-out transform hover:-translate-y-1 
                    hover:scale-110`}>
                        Switch to {isMultipleMode ? 'Single' : 'Multiple'} Mode
                    </button>
                </div>

                {/* Margin bottom */}
                <div className="mb-4">
                    {/* Block display, dark gray text, small text size, bold font, margin bottom */}
                    <label htmlFor="nomDeLaffaire" className="block text-gray-700 text-sm font-bold mb-2">
                        Nom de l'Affaire <span className="text-red-500"> * </span>
                    </label>

                    {/* Full width, padding, round border, shadow, dark gray text, leading tight, focus outline none, focus shadow outline */}
                    <input type="text" id="nomDeLaffaire" value={nomDeLaffaire}
                        onChange={(e) => setNomDeLaffaire(e.target.value)}
                        className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
                </div>

            {/* // ───────────────────────────────────────────────────────────────────────────── */}

                {/* Similar structure repeated for other form fields... */}
                <div className="mb-4">
                    <label htmlFor="department" className="block text-gray-700 text-sm font-bold mb-2">
                        Département
                    </label>
                    <select id="department" value={department}
                        onChange={(e) => setDepartment(e.target.value)} // here we assign the department choosen by the user, that eventually it will be used to search the commune
                        className="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                        <option value="">Choisissez un département</option> {/*  the option html element allow us to set each individual item in the selection list */}
                        {departments.map((dep) => (
                            <option key={dep.DEP_CODE} value={dep.DEP_CODE}>{`${dep.DEP_NOM} (${dep.DEP_CODE})`}</option> /* in the deparments useState variable array we have all departments, 
                                                                                                                             we will put them in the list programically with the map method  */
                        ))}
                    </select>
                </div>

            {/* // ───────────────────────────────────────────────────────────────────────────── */}

                <div className="mb-4">
                    <label htmlFor="commune" className="block text-gray-700 text-sm font-bold mb-2">
                        Commune
                    </label>
                    <select id="commune" value={commune}
                        onChange={(e) => setCommune(e.target.value)}
                        className="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                        <option value="">Select a commune</option>
                        {communes.map((com) => (
                            <option key={com.COM_CODE} value={com.COM_NOM}>{`${com.COM_NOM} (${com.COM_CODE})`}</option>
                        ))}
                    </select>
                </div>

            {/* // ───────────────────────────────────────────────────────────────────────────── */}

                <div className="mb-6">
                    <label htmlFor="precision" className="block text-gray-700 text-sm font-bold mb-2">
                        Précision <span className="text-red-500"> * </span>
                    </label>
                    <input type="text" id="precision" value={precision}
                        onChange={(e) => setPrecision(e.target.value)}
                        className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" />
                </div>

            {/* // ───────────────────────────────────────────────────────────────────────────── */}

                {/* Button with background color blue, on hover darker blue, white text, bold, padding, rounded corners, focus outline none, focus shadow outline */}
                <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded 
                focus:outline-none focus:shadow-outline transition duration-300 ease-in-out transform 
                hover:-translate-y-1 hover:scale-110 ">
                    Submit
                </button>
            </form>
        </div>
    );
}

export default AffaireForm;
