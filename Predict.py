def predict_smiles_from_excel(model, file_path, Superclass_mapping, Class_mapping, Subclass_mapping):
    try:
        df = pd.read_excel(file_path)
        if 'SMILES' in df.columns:
            smiles_list = df['SMILES'].tolist()
            predictions = []
            for smiles in smiles_list:
                predicted_results = predict_smiles(model, smiles, Superclass_mapping, Class_mapping, Subclass_mapping)
                predictions.append(predicted_results)
            return predictions, None
        else:
            return None, "Error: Column 'SMILES' not found in the Excel file."
    except FileNotFoundError:
        return None, f"Error: File not found at the specified path: {file_path}"
    except Exception as e:
        return None, f"Error occurred while processing the file: {e}"
    # File uploader for Excel file
    elif option == 'Upload Excel file':
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            # To read file as bytes:
            bytes_data = uploaded_file.getvalue()
            st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    # Save the uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.getvalue())
            temp_file_path = temp_file.name
        
        # Read Excel file and predict SMILES
    try:
            predictions, error = predict_smiles_from_excel(model, temp_file_path, Superclass_mapping, Class_mapping, Subclass_mapping)

            # Display predictions or error message
            if error:
                st.error(error)
            else:
                st.subheader("Predictions:")
                for idx, pred in enumerate(predictions):
                    st.write(f"Prediction {idx + 1}: Superclass= {pred[0]}, Class= {pred[1]}, Subclass= {pred[2]}")
    except Exception as e:
            st.error(f"Error occurred: {e}")
    finally:
            # Clean up the temporary file
            if temp_file_path and os.path.exists(temp_file_path):
                os.remove(temp_file_path)