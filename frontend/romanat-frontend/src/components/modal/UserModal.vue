<template>
  <div v-if="isOpen" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm">
    <div class="bg-white rounded-2xl w-full max-w-2xl mx-4 max-h-[90vh] overflow-y-auto shadow-2xl">
      <!-- Header -->
      <div class="sticky top-0 bg-white border-b border-gray-200 p-6 rounded-t-2xl">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold text-gray-900">
              {{ mode === 'edit' ? 'Edit User' : 'Create New User' }}
            </h2>
            <p class="text-gray-600 mt-1">
              {{ mode === 'edit' ? 'Update user information and permissions' : 'Add a new user to the system' }}
            </p>
          </div>
          <button 
            @click="$emit('close')" 
            class="text-gray-400 hover:text-gray-600 transition-colors p-2 hover:bg-gray-100 rounded-lg"
          >
            <span class="material-symbols-outlined text-2xl">close</span>
          </button>
        </div>
      </div>

      <!-- Form -->
      <form @submit.prevent="submitForm" class="p-6">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <!-- Personal Information -->
          <div class="md:col-span-2">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">Personal Information</h3>
          </div>
<!-- 
          <div class="md:col-span-2">
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Avatar
            </label>
            <div class="flex items-center gap-4">
              <img 
                :src="form.avatar || '/api/placeholder/80/80'" 
                class="w-20 h-20 rounded-full object-cover border-2 border-gray-300"
                alt="User avatar"
              >
              <div>
                <input
                  type="file"
                  @change="handleAvatarUpload"
                  accept="image/*"
                  class="hidden"
                  ref="avatarInput"
                >
                <button
                  type="button"
                  @click="$refs.avatarInput.click()"
                  class="bg-gray-100 text-gray-700 px-4 py-2 rounded-lg hover:bg-gray-200 transition-colors"
                >
                  Change Avatar
                </button>
                <p class="text-xs text-gray-500 mt-1">JPG, PNG or GIF, max 2MB</p>
              </div>
            </div>
          </div> -->

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              First Name <span class="text-red-500">*</span>
            </label>
            <input
              type="text"
              v-model="form.first_name"
              placeholder="Enter first name"
              class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-[#0f766e]/50 focus:border-transparent transition-colors duration-300"
              required
            >
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Last Name <span class="text-red-500">*</span>
            </label>
            <input
              type="text"
              v-model="form.last_name"
              placeholder="Enter last name"
              class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-[#0f766e]/50 focus:border-transparent transition-colors duration-300"
              required
            >
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Username <span class="text-red-500">*</span>
            </label>
            <input
              type="text"
              v-model="form.username"
              placeholder="Enter username"
              class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-[#0f766e]/50 focus:border-transparent transition-colors duration-300"
              required
            >
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Email Address <span class="text-red-500">*</span>
            </label>
            <input
              type="email"
              v-model="form.email"
              placeholder="Enter email address"
              class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-[#0f766e]/50 focus:border-transparent transition-colors duration-300"
              required
            >
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Phone Number
            </label>
            <input
              type="tel"
              v-model="form.phone"
              placeholder="Enter phone number"
              class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-[#0f766e]/50 focus:border-transparent transition-colors duration-300"
            >
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Address
            </label>
            <input
              type="text"
              v-model="form.address"
              placeholder="Enter phone number"
              class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-[#0f766e]/50 focus:border-transparent transition-colors duration-300"
            >
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Date of Birth
            </label>
            <input
              type="date"
              v-model="form.date_of_birth"
              placeholder="Enter phone number"
              class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-[#0f766e]/50 focus:border-transparent transition-colors duration-300"
            >
          </div>

          <!-- <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Role
            </label>
            <select
              v-model="form.department"
              class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-[#0f766e]/50 focus:border-transparent transition-colors duration-300"
            >
              <option value="">Select Role</option>
              <option value="Management">Manager</option>
              <option value="Front Desk">Receptionist</option>
            </select>
          </div> -->

          <!-- Role and Permissions -->
          <div class="md:col-span-2 border-t border-gray-200 pt-6">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">Role</h3>
          </div>

          <div class="md:col-span-2">
            <label class="block text-sm font-medium text-gray-700 mb-2">
              User Role <span class="text-red-500">*</span>
            </label>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
              <div
                v-for="role in roleOptions"
                :key="role.value"
                @click="form.role_id = role.value"
                class="border-2 rounded-xl p-4 cursor-pointer transition-all duration-300 hover:shadow-md"
                :class="form.role_id === role.value 
                  ? 'border-[#0f766e] bg-[#0f766e]/5' 
                  : 'border-gray-200 hover:border-gray-300'"
              >
                <div class="flex items-center gap-3">
                  <div class="flex items-center justify-center w-8 h-8 rounded-full border-2"
                       :class="form.role_id === role.value ? 'border-[#0f766e] bg-[#0f766e]' : 'border-gray-300'">
                    <span v-if="form.role_id === role.value" class="material-symbols-outlined text-white text-sm">
                      check
                    </span>
                  </div>
                  <div>
                    <p class="font-medium text-gray-900">{{ role.label }}</p>
                    <p class="text-sm text-gray-500">{{ role.description }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Permissions -->
          <!-- <div class="md:col-span-2">
            <label class="block text-sm font-medium text-gray-700 mb-3">
              Permissions
            </label>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 p-4 bg-gray-50 rounded-xl">
              <div v-for="permission in permissionOptions" :key="permission.value" class="flex items-center">
                <input
                  type="checkbox"
                  :value="permission.value"
                  v-model="form.permissions"
                  :id="'permission-' + permission.value"
                  class="w-4 h-4 text-[#0f766e] border-gray-300 rounded focus:ring-[#0f766e]/50"
                >
                <label :for="'permission-' + permission.value" class="ml-3 text-sm text-gray-700">
                  {{ permission.label }}
                </label>
              </div>
            </div>
          </div> -->

          <!-- Account Settings -->
          <div class="md:col-span-2 border-t border-gray-200 pt-6">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">Account Settings</h3>
          </div>

          <div v-if="mode === 'create'" class="md:col-span-2 gap-6">
        <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
             Password <span class="text-red-500">*</span>
            </label>
            <input
              type="password"
              v-model="form.password"
              placeholder="Enter temporary password"
              class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-[#0f766e]/50 focus:border-transparent transition-colors duration-300"
              :required="mode === 'create'"
            >
            </div>
            <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
            Confirm Password <span class="text-red-500">*</span>
            </label>
            <input
              type="password"
              v-model="form.password"
              placeholder="Enter temporary password"
              class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-[#0f766e]/50 focus:border-transparent transition-colors duration-300"
              :required="mode === 'create'"
            >
            </div>
            <p class="text-xs text-gray-500 mt-1">User will be required to change password on first login</p>
            
          </div>

          <div class="md:col-span-2">
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Account Status
            </label>
            <div class="flex items-center gap-6">
              <label class="flex items-center">
                <input
                  type="radio"
                  v-model="form.status"
                  value="active"
                  class="w-4 h-4 text-[#0f766e] border-gray-300 focus:ring-[#0f766e]/50"
                >
                <span class="ml-2 text-sm text-gray-700">Active</span>
              </label>
              <label class="flex items-center">
                <input
                  type="radio"
                  v-model="form.status"
                  value="inactive"
                  class="w-4 h-4 text-[#0f766e] border-gray-300 focus:ring-[#0f766e]/50"
                >
                <span class="ml-2 text-sm text-gray-700">Inactive</span>
              </label>
            </div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="flex gap-3 pt-6 mt-6 border-t border-gray-200">
          <button
            type="button"
            @click="$emit('close')"
            class="flex-1 bg-gray-100 text-gray-700 py-3 px-4 rounded-xl hover:bg-gray-200 transition-all duration-300 font-medium"
          >
            Cancel
          </button>
          <button
            type="submit"
            class="flex-1 bg-[#0f766e] text-white py-3 px-4 rounded-xl hover:bg-[#0f766e]/90 transition-all duration-300 font-medium shadow-lg hover:shadow-xl"
          >
            {{ mode === 'edit' ? 'Update User' : 'Create User' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { fetchRoles } from '../../api/auth/userApi';

export default {
  name: 'UserModal',
  props: {
    isOpen: Boolean,
    user: Object,
    mode: {
      type: String,
      default: 'create',
      validator: (value) => ['create', 'edit'].includes(value)
    }
  },

  data() {
    return {
      form: {
        first_name: '',
        last_name:'',
        username:'',
        email: '',
        phone: '',
        address: '',
        date_of_birth:'',
        role_id: '',
        password: '',
      },
      roleOptions: []  // <-- REQUIRED
    };
  },

  watch: {
    user: {
      immediate: true,
      handler(val) {
        if (val && this.mode === 'edit') {
          this.form = { ...this.form, ...val };
        } else {
          this.resetForm();
        }
      }
    },

    isOpen(val) {
      if (val) {
        this.getRoles();
      if (val && this.mode === 'create') {
        this.resetForm();
      }
    }}
  },

  mounted() {
    this.getRoles();     // <-- CALL API when modal loads
  },

  methods: {

    async getRoles() {
      try {
        const response = await fetchRoles(); 
console.log(response);
        const data = response.data;
console.log(data);

        this.roleOptions = data.map(role => ({
          value: role.id,
          label: role.name,
          description: role.description || 'System role'
        }));

      } catch (error) {
        console.error("Failed to fetch roles:", error);
        alert("Unable to load roles. Please check the backend.");
      }
    },

    resetForm() {
      this.form = {
        firstName: '',
        lastName:'',
        username:'',
        email: '',
        phone: '',
        address: '',
        birthDate:'',
        role: '',
        // status: 'active',
        password: '',
      };
    },

    submitForm() {
      if (!this.validateForm()) return;

      const userData = { ...this.form };

      if (this.mode === 'edit') {
        userData.id = this.user.id;
      }

      this.$emit('save', userData);
      this.$emit('close');
    },

    validateForm() {
      if (!this.form.first_name.trim() || !this.form.last_name.trim() || !this.form.username.trim()) {
        alert('Please enter full name and username');
        return false;
      }

      if (!this.form.email.trim()) {
        alert('Please enter an email');
        return false;
      }

      if (this.mode === 'create' && !this.form.password) {
        alert('Please enter a password');
        return false;
      }

      return true;
    },
  }
};
</script>
