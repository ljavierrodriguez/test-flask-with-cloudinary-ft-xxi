import React, { useEffect, useState } from 'react'
import * as config from './config'

const App = () => {
    const [portfolio, setPortfolio] = useState(1)
    const [photos, setPhotos] = useState(null)

    const [active, setActive] = useState(false)
    const [file, setFile] = useState(null)

    const [file2, setFile2] = useState(null)

    useEffect(() => {
        getPhotos();
    }, [])

    const getPhotos = () => {
        fetch(`http://127.0.0.1:5000/api/portfolios/${portfolio}/photos`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${config.token}`
            }
        })
            .then(response => response.json())
            .then(data => setPhotos(data))
            .catch(error => console.log(error.message));
    }

    const handleSubmit = e => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('active', active);
        formData.append('imagen', file)
        formData.append('listado', file2)

        uploadImage(formData);
        e.target.reset();
        setActive(false)
        setFile(null)

    }

    const handleSubmitUploadFile = e => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('listado', file2)

        uploadFile(formData);
        e.target.reset();
        setActive(false)
        setFile(null)

    }

    const uploadImage = async (data) => {
        try {
            const response = await fetch(`http://127.0.0.1:5000/api/portfolios/${portfolio}/photos`, {
                method: 'POST',
                body: data,
                headers: {
                    'Authorization': `Bearer ${config.token}`
                }
            })

            const result = await response.json()

            console.log(result);

            getPhotos()


        } catch (error) {
            console.log(error.message)
        }
    }

    const uploadFile = async (data) => {
        try {
            const response = await fetch(`http://127.0.0.1:5000/api/file-upload`, {
                method: 'POST',
                body: data,
                headers: {
                    'Authorization': `Bearer ${config.token}`
                }
            })

            const result = await response.json()

            console.log(result);

        } catch (error) {
            console.log(error.message)
        }
    }

    return (
        <div>
            <div className="w-75 mx-auto my-3 border border-1">
                <h4 className='m-2 p-2'>Upload Images</h4>
                <hr />
                <form onSubmit={handleSubmit} className='mx-2 p-2'>
                    <div className="form-group mb-3">
                        <label htmlFor="file" className="form-label">Imagen</label>
                        <input type="file" name="file" id="file" className='form-control' onChange={(e) => setFile(e.target.files[0])} />
                    </div>
                    <div className="form-group mb-3">
                        <div className="form-check form-switch">
                            <input className="form-check-input" type="checkbox" role="switch" id="active" name="active" checked={active ? true : false} onClick={() => setActive(!active)} />
                            <label className="form-check-label" htmlFor="active">Active</label>
                        </div>
                    </div>
                    <div className="d-grid">
                        <button className="btn btn-primary btn-sm gap-2">
                            Upload
                        </button>
                    </div>
                </form>
            </div>
            <div className="w-75 mx-auto my-3 border border-1">
                <h4 className='m-2 p-2'>Upload File</h4>
                <hr />
                <form onSubmit={handleSubmitUploadFile} className='mx-2 p-2'>
                    <div className="form-group mb-3">
                        <label htmlFor="file" className="form-label">Listado de Usuarios (csv)</label>
                        <input type="file" name="file2" id="file2" className='form-control' onChange={(e) => setFile2(e.target.files[0])} />
                    </div>
                    <div className="d-grid">
                        <button className="btn btn-primary btn-sm gap-2">
                            Upload
                        </button>
                    </div>
                </form>
            </div>
            <div className="w-75 mx-auto border border-1">
                <div className="w-100 d-flex justify-content-center">
                    {
                        !!photos &&
                        photos.map((photo) => {
                            return <img key={photo.id} src={photo.filename} alt="" className="img-fluid rounded-circle m-2" style={{ width: '100px', height: '100px', objectFit: 'cover'}} />
                        })
                    }
                </div>
            </div>
        </div>
    )
}

export default App