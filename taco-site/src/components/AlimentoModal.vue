<template>
    <div class="backdrop">
        <div class="modal">
            <p>Modal</p>
        </div>
    </div>
</template>

<style>
    .modal {
        width: 400px;
        padding: 20px;
        margin: 100px auto;
        background-color: white;
        border-radius: 10px;
    }

    .backdrop {
        position: fixed;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>