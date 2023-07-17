import React from 'react'
import { Nav } from '../components/NavBar/Nav'
import { Button } from '../UI/Button/Button'


export const Home =()=> {
    return (
        <div>
            <div>
                <Nav />
                <Button name='Login'/>
            </div>
        </div>
    )
}