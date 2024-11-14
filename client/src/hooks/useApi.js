import { useAlert } from './useAlert';
import axios from '../api';

export default function useApi() {
    const showAlert = useAlert();

    const callApi = async (url, config = {}) => {
        try{
            const response = await axios.get(url, config);
            const data = response.data;
            if(data.length === 0){
                showAlert('No records available on this page.')
            }
            return data;
        }
        catch(error){
            handleErrors(error);
            throw error;
        }
    };

    const handleErrors = (error) => {
        if(error.response){
            switch(error.status){
                case 404:
                    showAlert("User not found.");
                    break;
                case 429:
                    showAlert("Too many requests. Please try again later.");
                    break;
                case 500:
                    showAlert("Internal server error.");
                    break;
                case 401:
                    showAlert("Unauthorized access.");
                    break;
                case 400:
                    showAlert("Please enter a valid value in the search field.");
                    break;
                default:
                    showAlert("Some issue processing the request, Please try again later.");
            }
        }
        else{
            showAlert("Network error. Please check your connection.")
        }
    };

    return callApi;
}
