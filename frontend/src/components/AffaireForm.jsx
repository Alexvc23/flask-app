import React, { useEffect, useState } from 'react';
import axios from 'axios';

const apiAddress = "http://localhost:5000";

const AffaireForm = () => {
    const [nomDeLaffaire, setNomDeLaffaire] = useState('');
    const [department, setDepartment] = useState([]); // variable to store only the department choosen by the client 
    const [departments, setDepartments] = useState([]); // variable to store the stire department list
    // const [commune, setCommune] = useState('');
    // const [communes, setCommunes] = useState('');
    const [precision, setPrecision] = useState('');

   // const departments = ['department 1', 'department 2', 'department 3'];
    // let department = '';
    const communes = ['Commune A', 'Commune B', 'Commune C'];
    let commune = '';
    let selectedDepartment = '';

    /*
    
                 #       ####   ####    ##   #         ###### #    # #    #  ####  ##### #  ####  #    #  ####
                 #      #    # #    #  #  #  #         #      #    # ##   # #    #   #   # #    # ##   # #
                 #      #    # #      #    # #         #####  #    # # #  # #        #   # #    # # #  #  ####
                 #      #    # #      ###### #         #      #    # #  # # #        #   # #    # #  # #      #
                 #      #    # #    # #    # #         #      #    # #   ## #    #   #   # #    # #   ## #    #
                 ######  ####   ####  #    # ######    #       ####  #    #  ####    #   #  ####  #    #  ####
    
    */

    const fetchDepartments = async () => {
        fetch('http://localhost:5000/departement')
            .then(response => response.json())
            .then(data => {setDepartments(data); console.log(departments)})
            .catch(error => console.error('Error fetching departements:', error));
    }

    const fetchCommunes = async () => {
        if (department) {
            try {
                const response = await axios.get(`${apiAddress}/communes?dep_code=${department}`); // create http get call to fetch communs list 
            } catch (error) {
                console.error('Error fetching communes:', error);
            }
        }
    }
    // ─────────────────────────────────────────────────────────────────────────────

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
                {/* Margin bottom */}
                <div className="mb-4">
                    {/* Block display, dark gray text, small text size, bold font, margin bottom */}
                    <label htmlFor="nomDeLaffaire" className="block text-gray-700 text-sm font-bold mb-2">
                        Nom de l'Affaire
                    </label>
                    {/* Full width, padding, round border, shadow, dark gray text, leading tight, focus outline none, focus shadow outline */}
                    <input type="text" id="nomDeLaffaire" value={nomDeLaffaire}
                        onChange={(e) => setNomDeLaffaire(e.target.value)}
                        className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
                </div>

                {/* Similar structure repeated for other form fields... */}
                <div className="mb-4">
                    <label htmlFor="department" className="block text-gray-700 text-sm font-bold mb-2">
                        Département
                    </label>
                    <select id="department" value={department}
                        onChange={(e) => setDepartment(e.target.value)}
                        className="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                        <option value="">Choisissez un département</option>
                        {departments.map((dep) => (
                            <option key={dep.DEP_CODE} value={dep.DEP_CODE}>{`${dep.DEP_NOM} (${dep.DEP_CODE})`}</option>
                        ))}
                    </select>
                </div>


                <div className="mb-4">
                    <label htmlFor="commune" className="block text-gray-700 text-sm font-bold mb-2">
                        Commune
                    </label>
                    <select id="commune" value={commune}
                        // onChange={(e) => setCommune(e.target.value)}
                        className="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                        <option value="">Select a commune</option>
                        {/* {communes.map((com, index) => (
                            <option key={index} value={com}>{com}</option>
                        ))} */}
                    </select>
                </div>

                <div className="mb-6">
                    <label htmlFor="precision" className="block text-gray-700 text-sm font-bold mb-2">
                        Précision
                    </label>
                    <input type="text" id="precision" value={precision}
                        onChange={(e) => setPrecision(e.target.value)}
                        className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" />
                </div>

                {/* Button with background color blue, on hover darker blue, white text, bold, padding, rounded corners, focus outline none, focus shadow outline */}
                <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
                    Submit
                </button>
            </form>
        </div>
    );
}

export default AffaireForm;
