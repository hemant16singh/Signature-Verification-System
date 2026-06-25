import * as THREE from 'three';

// Scene setup
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x050510);

const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 30;

const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('bg-canvas'), alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(window.devicePixelRatio);

// Lighting
const ambientLight = new THREE.AmbientLight(0x404060);
scene.add(ambientLight);

const pointLight1 = new THREE.PointLight(0x00ffff, 1, 50);
pointLight1.position.set(10, 10, 10);
scene.add(pointLight1);

const pointLight2 = new THREE.PointLight(0xff00ff, 1, 50);
pointLight2.position.set(-10, -10, 10);
scene.add(pointLight2);

// Create floating particles
const particlesGeometry = new THREE.BufferGeometry();
const particlesCount = 2000;
const posArray = new Float32Array(particlesCount * 3);
const colorArray = new Float32Array(particlesCount * 3);

for(let i = 0; i < particlesCount * 3; i += 3) {
    // Position
    posArray[i] = (Math.random() - 0.5) * 100;
    posArray[i+1] = (Math.random() - 0.5) * 100;
    posArray[i+2] = (Math.random() - 0.5) * 100;
    
    // Color
    const color = new THREE.Color().setHSL(Math.random() * 0.2 + 0.5, 0.8, 0.5);
    colorArray[i] = color.r;
    colorArray[i+1] = color.g;
    colorArray[i+2] = color.b;
}

particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
particlesGeometry.setAttribute('color', new THREE.BufferAttribute(colorArray, 3));

const particlesMaterial = new THREE.PointsMaterial({
    size: 0.1,
    vertexColors: true,
    transparent: true,
    opacity: 0.8,
    blending: THREE.AdditiveBlending
});

const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
scene.add(particlesMesh);

// Create central geometric shapes
const geometry1 = new THREE.IcosahedronGeometry(3, 0);
const material1 = new THREE.MeshPhongMaterial({
    color: 0x00ffff,
    emissive: 0x004444,
    wireframe: true,
    transparent: true,
    opacity: 0.3
});
const shape1 = new THREE.Mesh(geometry1, material1);
scene.add(shape1);

const geometry2 = new THREE.TorusKnotGeometry(2, 0.5, 100, 16);
const material2 = new THREE.MeshPhongMaterial({
    color: 0xff00ff,
    emissive: 0x440044,
    wireframe: true,
    transparent: true,
    opacity: 0.3
});
const shape2 = new THREE.Mesh(geometry2, material2);
scene.add(shape2);

// Add some floating lines
const linesGeometry = new THREE.BufferGeometry();
const linesPositions = new Float32Array(300 * 3 * 2); // 300 lines with 2 points each

for(let i = 0; i < 300; i++) {
    const x = (Math.random() - 0.5) * 60;
    const y = (Math.random() - 0.5) * 60;
    const z = (Math.random() - 0.5) * 60;
    
    linesPositions[i*6] = x;
    linesPositions[i*6+1] = y;
    linesPositions[i*6+2] = z;
    
    linesPositions[i*6+3] = x + (Math.random() - 0.5) * 10;
    linesPositions[i*6+4] = y + (Math.random() - 0.5) * 10;
    linesPositions[i*6+5] = z + (Math.random() - 0.5) * 10;
}

linesGeometry.setAttribute('position', new THREE.BufferAttribute(linesPositions, 3));
const linesMaterial = new THREE.LineBasicMaterial({ color: 0x3366ff, opacity: 0.1, transparent: true });
const lines = new THREE.LineSegments(linesGeometry, linesMaterial);
scene.add(lines);

// Mouse interaction
let mouseX = 0;
let mouseY = 0;

document.addEventListener('mousemove', (event) => {
    mouseX = (event.clientX / window.innerWidth - 0.5) * 2;
    mouseY = (event.clientY / window.innerHeight - 0.5) * 2;
});

// Animation loop
function animate() {
    requestAnimationFrame(animate);
    
    // Rotate shapes
    shape1.rotation.x += 0.001;
    shape1.rotation.y += 0.002;
    shape2.rotation.x += 0.002;
    shape2.rotation.y += 0.001;
    
    // Rotate particles
    particlesMesh.rotation.y += 0.0002;
    particlesMesh.rotation.x += 0.0001;
    
    // Rotate lines
    lines.rotation.y += 0.0003;
    lines.rotation.x += 0.0002;
    
    // Smooth camera follow
    camera.position.x += (mouseX * 10 - camera.position.x) * 0.02;
    camera.position.y += (-mouseY * 10 - camera.position.y) * 0.02;
    camera.lookAt(scene.position);
    
    renderer.render(scene, camera);
}

animate();

// Handle window resize
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});