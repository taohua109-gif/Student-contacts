// API基础URL
const API_BASE_URL = 'http://127.0.0.1:5000/api';

// 全局变量
let contacts = [];
let groups = [];
let currentView = 'contacts';
let currentGroup = null;
let currentContactId = null;
let viewMode = 'grid';

// DOM元素
const contactsView = document.getElementById('contacts-view');
const groupsView = document.getElementById('groups-view');
const contactsGrid = document.getElementById('contacts-grid');
const contactsTableBody = document.getElementById('contacts-table-body');
const groupsList = document.getElementById('groups-list');
const groupsContent = document.getElementById('groups-content');
const contactModal = document.getElementById('contact-modal');
const deleteModal = document.getElementById('delete-modal');
const contactForm = document.getElementById('contact-form');
const addContactBtn = document.getElementById('add-contact-btn');

// 初始化应用
document.addEventListener('DOMContentLoaded', () => {
    loadContactsFromAPI();
    bindEvents();
});

// API调用函数
async function loadContactsFromAPI() {
    try {
        const response = await fetch(`${API_BASE_URL}/contacts`);
        if (!response.ok) throw new Error('Failed to fetch contacts');
        contacts = await response.json();
        groups = [...new Set(contacts.map(c => c.group))];
        renderContacts();
        renderGroups();
    } catch (error) {
        console.error('Error loading contacts:', error);
        showToast('Failed to load contacts');
    }
}

// 其他API函数和渲染逻辑...
// (这里包含之前修改的所有JavaScript逻辑)
