import React, { createContext, useContext, useState } from 'react';
import Alert from 'react-bootstrap/Alert'

const AlertContext = createContext()

export const AlertProvider = ({ children }) => {
    const [alert, setAlert] = useState({ message: '', variant: '' });
  
    const showAlert = (message, variant = 'danger') => {
      setAlert({ message, variant });
    };
  
    const handleCloseAlert = () => {
      setAlert({ message: '', variant: '' });
    };
  
    return (
      <AlertContext.Provider value={showAlert}>
        {alert.message && (
          <Alert
            variant={alert.variant}
            onClose={handleCloseAlert}
            dismissible
            className="position-fixed top-0 start-50 translate-middle-x mt-5"
            style={{ zIndex: 1050, width: '40%' }}
          >
            {alert.message}
          </Alert>
        )}
        {children}
      </AlertContext.Provider>
    );
};
  
export const useAlert = () => {
    return useContext(AlertContext);
};
